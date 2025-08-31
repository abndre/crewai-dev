from fastapi import FastAPI
from pydantic import BaseModel, Field
from .crew import Corinthias   # importa do seu crew.py
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env da raiz do projeto
load_dotenv(dotenv_path=".env")  # ajuste o caminho se necessário

app = FastAPI()

class InputData(BaseModel):
    topic: str = Field("Qual a idade do Corinthians?", description="O tópico da pergunta")

@app.post("/run")
async def run_crew(data: InputData):
    try:
        crew = Corinthias().crew()
        result = crew.kickoff(inputs={"topic": data.topic})
        return {"result": str(result)}
    except Exception as e:
        return {"error": str(e)}
