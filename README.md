# Projeto de desenvolvimento  com  CrewAI


Para IA estou utilizando  Ollama

- modelo:  ollama3

## Projetos

### Corinthias

Neste projeto estou criando um agente  especialista em  Futebol, mas  com o time  corinthias.
Tambem estou desenvolvendo uma  API com fastapi para deploy

```
cd corinthias
crewai run # para testar
```

Fast-API
```
cd corinthias
uvicorn src.corinthias.api:app --reload
```

```
curl -X 'POST' \
  'http://127.0.0.1:8000/run' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "Qual a idade do Corinthians?"
}'
```

Ou no navegador: http://127.0.0.1:8000/docs

#### Funcionamento do  modelo

Foi criado um agente  e uma  task

O agente tem foco em parametros a respeito do  contexto.
/corinthias/src/corinthias/config/agents.yaml

A task contem os parametros de  como eu espero a resposta, baseado no topico.
/corinthias/src/corinthias/config/task.yaml