from fastapi import FastAPI
from funciones import PlayTimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UsersWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Machine Learning Operations (MLOps)"}

@app.get("/PlayTimeGenre/{genero}")
async def User(genero: str):
    try:
        resultado = PlayTimeGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   

@app.get("/UserForGenre/{genero}")
async def User(genero: str):
    try:
        resultado = UserForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   
    
@app.get("/UsersRecommend/{anio}")
async def User(anio: int):
    try:
        anio=int(anio)
        resultado = UsersRecommend(anio)
        return resultado
    except Exception as e:
        return {"Año debe ser un entero": str(e)}   
    
@app.get("/UsersWorstDeveloper/{anio}")
async def User(anio: int):
    try:
        anio=int(anio)
        resultado = UsersWorstDeveloper(anio)
        return resultado
    except Exception as e:
        return {"Año debe ser un entero": str(e)}   
    
@app.get("/sentiment_analysis/{empresa_desarrolladora}")
async def User(empresa_desarrolladora: str):
    try:
        resultado = sentiment_analysis(empresa_desarrolladora)
        return resultado
    except Exception as e:
        return {"error": str(e)}  
    
@app.get("/recomendacion_juego/{id}")
async def recomendacion(id: int):
    try:
        id=int(id)
        resultado = recomendacion_juego(id)
        return resultado
    except Exception as e:
        return {"Id debe ser un entero": str(e)} 