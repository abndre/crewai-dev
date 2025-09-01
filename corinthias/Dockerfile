# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copia pyproject e lock para instalar dependências primeiro
# COPY pyproject.toml uv.lock ./

# # Instala dependências
# RUN pip install --upgrade pip
# RUN pip install .

# # Copia todo o código
# COPY src/ ./src
# #COPY config/ ./config
# COPY knowledge/ ./knowledge



# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the PYTHONPATH to include src/
ENV PYTHONPATH=/app/src

# Copy the application code
COPY src .

RUN crewai install

# Expose the app port
#EXPOSE 5000

# Specify the command to run on container start
# CMD ["crewai", "run"]

# # Set the entrypoint to crewai
# ENTRYPOINT ["crewai"]

# # Default to "run" if no command is provided
# CMD ["run"]

# Expõe porta FastAPI
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "corinthias.api:app", "--host", "0.0.0.0", "--port", "8000"]