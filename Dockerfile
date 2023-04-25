# Utilice una imagen base de Python
FROM python:3.9

# Establezca un directorio de trabajo
WORKDIR /app

# Copie los archivos de requerimientos y el código
COPY requirements.txt /app
COPY . /app

# Instale las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecute la aplicación Flask
CMD ["python", "feedback_api.py"]
