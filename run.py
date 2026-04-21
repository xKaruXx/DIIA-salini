import uvicorn
import os
import argparse
from dotenv import load_dotenv

# Este script poner en marcha el servidor web el cual hospeda a mi aplicación FastAPI.

# Cargar variables de entorno
load_dotenv()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar el servidor de chatbot de Coradir")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host para el servidor")
    parser.add_argument("--port", type=int, default=8850, help="Puerto para el servidor")
    parser.add_argument("--reload", action="store_true", help="Habilitar recarga automática")
    
    args = parser.parse_args()
    
    # Asegurar que existen los directorios necesarios
    os.makedirs("dataset", exist_ok=True)
    os.makedirs("chat_assets", exist_ok=True)
    
    print(f"Iniciando servidor en http://{args.host}:{args.port}")
    
    uvicorn.run(
        "api.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level="info"
    )