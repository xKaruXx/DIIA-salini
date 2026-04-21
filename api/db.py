import logging
import os
import datetime

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Index, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

logger = logging.getLogger(__name__)

# Configura la conexión a la base de datos
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chatbot_movilidad.db")

if not os.getenv("DATABASE_URL"):
    logger.warning("DATABASE_URL no configurada. Se usar\u00e1 SQLite local en chatbot_movilidad.db")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos
class ChatSession(Base):
    __tablename__ = "chat_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String(36), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    start_time = Column(DateTime, default=datetime.datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id", ondelete="CASCADE"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    sender = Column(String(10), nullable=False)  # 'user' o 'bot'
    message = Column(Text, nullable=False)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String(36), unique=True, nullable=False)
    email = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    phone = Column(String(20), nullable=True)
    name = Column(String(100), nullable=True) 
    ip_address = Column(String(45), nullable=True) 

class UserAnalysis(Base):
    __tablename__ = "user_analysis"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    analysis_date = Column(DateTime, default=datetime.datetime.utcnow)
    conversation_summary = Column(Text, nullable=True)
    user_type = Column(String(50), nullable=True)
    primary_interest = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    name = Column(String(100), nullable=True)  
    ip_address = Column(String(45), nullable=True)  

# Índices
Index('idx_users_client_id', User.client_id)
Index('idx_users_email', User.email)
Index('idx_user_analysis_user_id', 'user_id'),

# Crea las tablas si no existen
def create_tables():
    Base.metadata.create_all(bind=engine)

# Obtiene una sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Funciones de utilidad para trabajar con la base de datos
def get_or_create_chat_session(db, client_id):
    """Busca una sesión existente o crea una nueva"""
    # Primero, asegurarnos de tener el usuario correcto
    user = get_or_create_user(db, client_id)
    
    # Buscar una sesión para este client_id que esté asociada al usuario correcto
    session = db.query(ChatSession).filter(
        ChatSession.client_id == client_id,
        ChatSession.user_id == user.id
    ).first()
    
    if not session:
        # Crear nueva sesión con referencia explícita al usuario
        session = ChatSession(
            client_id=client_id, 
            user_id=user.id
        )
        db.add(session)
        db.commit()
        db.refresh(session)
    else:
        # Actualiza last_activity
        session.last_activity = datetime.datetime.utcnow()
        db.commit()
    
    return session

def save_chat_message(db, session_id, sender, message):
    """Guarda un mensaje en la base de datos"""
    db_message = ChatMessage(
        session_id=session_id,
        sender=sender,
        message=message
    )
    db.add(db_message)
    db.commit()
    return db_message

# Funciones para usuarios
def get_or_create_user(db, client_id):
    """Busca un usuario existente o crea uno nuevo"""
    user = db.query(User).filter(User.client_id == client_id).first()
    if not user:
        user = User(client_id=client_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def update_user_info(db, client_id, **kwargs):
    """Actualiza la información de un usuario"""
    user = get_or_create_user(db, client_id)
    
    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    db.commit()
    db.refresh(user)
    return user

def get_user_info(db, client_id):
    """Obtiene la información de un usuario"""
    user = db.query(User).filter(User.client_id == client_id).first()
    return user
