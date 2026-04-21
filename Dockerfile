FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código, incluyendo los assets
COPY . .

# Asegurarnos de que los directorios existan y tengan permisos adecuados
RUN mkdir -p chroma_db && chmod -R 755 chat_assets

# Puerto dinámico (se configura desde Portainer, por defecto uso el 8851, pero va a cambiar según la configuración de Portainer, este corresponde al puerto a la pagina real de movilidad)
EXPOSE ${PORT:-8851}

# Comando dinámico - usa la variable PORT de Portainer
CMD python run.py --host 0.0.0.0 --port ${PORT:-8851}