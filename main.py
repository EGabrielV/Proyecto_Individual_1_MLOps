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
    mensaje = (
        "Machine Learning Operations (MLOps)\n"
        "Funciones disponibles: \n"
        " \n \PlayTimeGenre\( genero : str ): \n"
        "   Devuelve `año` con mas horas jugadas para dicho género."
        " \n \UserForGenre\( genero : str ): \n"
        "   Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año."
        " \n \UsersRecommend\( año : int ): \n "
        "   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)"
        " \n \UsersWorstDeveloper\( año : int ): \n"
        "   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado."
        " \n \sentiment_analysis( empresa desarrolladora : str ): \n "
        "Devuelve el nombre de la desarrolladora y una lista de la suma de análisis de sentimiento."
        "**Sistema de recomendación item-item:**"
              " \n \recomendacion_juego( id de producto ): \n"
        "   Devuelve una lista con 5 juegos recomendados similares al ingresado."
              )
    return {"message": mensaje}

@app.get("/PlayTimeGenre/{genero}")
async def User(genero: str):
    try:
        resultado = PlayTimeGenre(genero)
        return str(resultado)
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