# Construya la imagen de Docker
docker build -t ia-modificacion-codigo .

# Ejecute el contenedor en un entorno aislado con el puerto 8000 expuesto
docker run --rm -it -p 8000:8000 ia-modificacion-codigo
