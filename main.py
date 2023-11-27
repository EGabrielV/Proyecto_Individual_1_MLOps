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
        "Machine Learning Operations (MLOps)"
    )
    return {"message": mensaje}

@app.get("/PlayTimeGenre/{genero}", tags=['PlayTimeGenre'])
async def User(genero: str):
    """
    Devuelve el año de lanzamiento correspondiente al género proporcionado.

    Parámetros:
    - genero (str): El género para el cual se busca el año de lanzamiento.

    Devoluciones:
    - int: El año de lanzamiento correspondiente al género.
    - str: Mensaje de error si el género no se encuentra en la consulta.
    """
    try:
        resultado = PlayTimeGenre(genero)
        return str(resultado)
    except Exception as e:
        return {"error": str(e)}   

@app.get("/UserForGenre/{genero}", tags=['UserForGenre'])
async def User(genero: str):
    """
    Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

    Parámetros:
    - genero (str): El género para el cual se busca el usuario con más horas jugadas.

    Retorna:
    - str: El nombre del usuario que acumula más horas jugadas para el género dado.
    - str: En caso de que el género no esté en la lista predefinida.

    Lista de Géneros Válidos:
    'Action', 'Casual', 'Indie', 'Simulation', 'Strategy', 'Free to Play', 'RPG', 'Sports',
    'Adventure', 'Racing', 'Early Access', 'Massively Multiplayer', 'Animation & Modeling',
    'Video Production', 'Utilities', 'Web Publishing', 'Education', 'Software Training',
    'Design & Illustration', 'Audio Production', 'Photo Editing'
    """
    try:
        resultado = UserForGenre(genero)
        return resultado
    except Exception as e:
        return {"error": str(e)}   
    
@app.get("/UsersRecommend/{anio}", tags=['UsersRecommend'])
async def User(anio: int):
    """
    Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.

    Parámetros:
    - año (int): El año para el cual se busca obtener el top 3 de juegos recomendados.

    Retorna:
    - list: Una lista de diccionarios, donde cada diccionario representa un juego en el top 3.
            Cada diccionario tiene una clave que indica el puesto (Puesto 1, Puesto 2, Puesto 3)
            y un valor que representa el nombre del juego.

    Nota:
    - Si el año no se encuentra en el conjunto de datos, se devuelve un diccionario con el mensaje "Año no encontrado en el conjunto de datos".
    """
    try:
        anio=int(anio)
        resultado = UsersRecommend(anio)
        return resultado
    except Exception as e:
        return {"Año debe ser un entero": str(e)}   
    
@app.get("/UsersWorstDeveloper/{anio}", tags=['UsersWorstDeveloper'])
async def User(anio: int):
    """
    Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.

    Parámetros:
    - año (int): El año para el cual se busca obtener el top 3 de desarrolladoras con juegos menos recomendados.

    Retorna:
    - list: Una lista de diccionarios, donde cada diccionario representa una desarrolladora en el top 3.
            Cada diccionario tiene una clave que indica el puesto (Puesto 1, Puesto 2, Puesto 3)
            y un valor que representa el nombre de la desarrolladora.

    Nota:
    - Si el año no se encuentra en el conjunto de datos, se devuelve un diccionario con el mensaje "Año no encontrado en el conjunto de datos".
    """
    try:
        anio=int(anio)
        resultado = UsersWorstDeveloper(anio)
        return resultado
    except Exception as e:
        return {"Año debe ser un entero": str(e)}   
    
@app.get("/sentiment_analysis/{empresa_desarrolladora}", tags=['sentiment_analysis'])
async def User(empresa_desarrolladora: str):
    """
    Devuelve el nombre de la desarrolladora y una lista de la suma de análisis de sentimiento.

    Parámetros:
    - empresa_desarrolladora (str): El nombre de la desarrolladora para la cual se busca el análisis de sentimiento.

    Retorna:
    - dict: Un diccionario que contiene el nombre de la desarrolladora y una lista de la suma de análisis de sentimiento.
            La lista tiene tres elementos: Negative, Neutral, y Positive.

    Nota:
    - Si la desarrolladora no se encuentra en la consulta, se devuelve un diccionario con un mensaje de error.
    """
    try:
        resultado = sentiment_analysis(empresa_desarrolladora)
        return resultado
    except Exception as e:
        return {"error": str(e)}  
    
@app.get("/recomendacion_juego/{id}", tags=['recomendacion_juego'])
async def recomendacion(id: int):
    """
    Devuelve una lista con 5 juegos recomendados similares al ingresado.

    Parámetros:
    - id (int): El identificador único del juego para el cual se busca obtener recomendaciones.

    Retorna:
    - str: Una cadena que contiene la lista de 5 juegos recomendados similares al juego con el ID proporcionado.
            La cadena está en el formato de la consulta y puede necesitar ser procesada según los requisitos.

    Nota:
    - Si el ID no se encuentra en la consulta, se devuelve una cadena indicando que el ID no se ha encontrado.
    """
    try:
        id=int(id)
        resultado = recomendacion_juego(id)
        return resultado
    except Exception as e:
        return {"Id debe ser un entero": str(e)} 