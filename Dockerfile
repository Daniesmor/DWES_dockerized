# Usa una imagen oficial de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Instala Java (necesario para ANTLR) y otras dependencias
RUN apt-get update && apt-get install -y \
    default-jdk \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Descarga el JAR de ANTLR
RUN curl -o /usr/local/lib/antlr-4.10.1-complete.jar https://www.antlr.org/download/antlr-4.10.1-complete.jar

# Copia los archivos de la aplicación (incluyendo Scratch.g4 y analysis.py)
COPY . .

# Genera el lexer y parser a partir del archivo Scratch.g4
#RUN java -cp /usr/local/lib/antlr-4.10.1-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 Scratch.g4

# Instala las dependencias de Python (incluyendo antlr4-python3-runtime, xlwt y openpyxl)
RUN pip install --no-cache-dir antlr4-python3-runtime==4.10 xlwt openpyxl

# Comando por defecto para ejecutar la aplicación
CMD ["bash"]
