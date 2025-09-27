from fastapi import FastAPI
import pandas as pd

# Carregando o dataset
df = pd.read_csv("Dataset.csv")

# Inicializando a API
app = FastAPI()

# Endpoint básico
@app.get("/")
def home():
    return {
        "projeto": "API Pokémon",
        "autor": "Andre",
        "descricao": "API para servir dados de Pokémon",
        "total_registros": len(df)
    }

# Endpoint que lista todos os dados
@app.get("/dados")
def listar_todos():
    return df.to_dict(orient="records")

# Endpoint intermediário: busca por ID
@app.get("/dados/{item_id}")
def buscar_por_id(item_id: int):
    resultado = df[df["#"] == item_id]
    if resultado.empty:
        return {"erro": "Pokémon não encontrado"}
    return resultado.to_dict(orient="records")[0]
