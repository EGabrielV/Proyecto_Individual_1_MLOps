import pandas as pd

#------Funciones:


#Funcion 1:
def PlayTimeGenre(genero: str):
    """
    Devuelve el año de lanzamiento correspondiente al género proporcionado.

    Parámetros:
    - genero (str): El género para el cual se busca el año de lanzamiento.

    Devoluciones:
    - int: El año de lanzamiento correspondiente al género.
    - str: Mensaje de error si el género no se encuentra en la consulta.
    """
    # Leer el archivo CSV
    Consulta1 = pd.read_csv('Consultas/Consulta1.csv')

    try:
        # Intentar encontrar el índice del género
        indice = Consulta1[Consulta1['genero'] == genero].index[0]

        # Obtener el año de lanzamiento correspondiente al índice del género
        año = Consulta1['año_lanzamiento'][indice]

        return año

    except IndexError:
        # Capturar la excepción si no se encuentra el género
        mensaje_error = f'''No se encontró el género '{genero}' en la consulta. 
Lista de Generos: 'Action', 'Casual', 'Indie', 'Simulation', 'Strategy', 'Free to Play', 'RPG', 'Sports', 'Adventure', 'Racing', 'Early Access', 'Massively Multiplayer', 'Animation & Modeling', 'Video Production', 'Utilities', 'Web Publishing', 'Education', 'Software Training', 'Design & Illustration', 'Audio Production', 'Photo Editing' '''
        return mensaje_error



#Funcion 2:
def UserForGenre(genero: str):
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
    Consulta2 = pd.read_csv('Consultas/Consulta2.csv')

    # En caso que la entrada no sea un género válido
    if genero not in ['Action', 'Casual', 'Indie', 'Simulation', 'Strategy', 'Free to Play', 'RPG', 'Sports',
                      'Adventure', 'Racing', 'Early Access', 'Massively Multiplayer', 'Animation & Modeling',
                      'Video Production', 'Utilities', 'Web Publishing', 'Education', 'Software Training',
                      'Design & Illustration', 'Audio Production', 'Photo Editing']:
        # Si no está en la lista, lanza una excepción
        return (f"No se encontró el género '{genero}' en la consulta."
                "\n Lista de Géneros Válidos: 'Action', 'Casual', 'Indie', 'Simulation', 'Strategy', "
                "'Free to Play', 'RPG', 'Sports', 'Adventure', 'Racing', 'Early Access', "
                "'Massively Multiplayer', 'Animation & Modeling', 'Video Production', 'Utilities', "
                "'Web Publishing', 'Education', 'Software Training', 'Design & Illustration', "
                "'Audio Production', 'Photo Editing'"
                )

    # Filtra el DataFrame para obtener la respuesta correspondiente al género
    resultado = Consulta2['respuesta'][Consulta2['genero'] == genero]
    
    # Retorna el resultado (nombre del usuario)
    return resultado.iloc[0]




#Funcion 3:   
def UsersRecommend(año: int):
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
    Consulta3 = pd.read_csv('Consultas/Consulta3.csv')

    # Verifica si el año está dentro del rango en el conjunto de datos
    if año < Consulta3['año'].min() or año > Consulta3['año'].max():
        return {"Año no encontrado en el conjunto de datos"}

    # Filtramos para el año de interés
    filtered_df = Consulta3[Consulta3['año'] == año]

    # Seleccionar las 3 aplicaciones con más revisiones positivas
    top_apps = filtered_df['app_name'].value_counts().head(3).index

    # Crea la lista de juegos en el top 3
    lista = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(top_apps)]

    return lista




#Funcion 4:
def UsersWorstDeveloper(año: int):
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
    Consulta4 = pd.read_csv('Consultas/Consulta4.csv')

    # Verifica si el año está dentro del rango en el conjunto de datos
    if año < Consulta4['año'].min() or año > Consulta4['año'].max():
        return {"Año no encontrado en el conjunto de datos"}

    # Filtramos para el año de interés
    filtered_df = Consulta4[Consulta4['año'] == año]

    # Seleccionar las 3 desarrolladoras con menos revisiones positivas
    top_worst_devs = filtered_df['developer'].value_counts().head(3).index

    # Crea la lista de desarrolladoras en el top 3
    lista = [{"Puesto {}".format(i + 1): developer} for i, developer in enumerate(top_worst_devs)]

    return lista




#Funcion 5:
def sentiment_analysis(empresa_desarrolladora: str):
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
    Consulta5 = pd.read_csv('Consultas/Consulta5.csv')

    try:
        # Filtrar el DataFrame para obtener el análisis de sentimiento de la desarrolladora
        emp = Consulta5[Consulta5['developer'] == empresa_desarrolladora]

        # Crear un diccionario con el nombre de la desarrolladora y el análisis de sentimiento
        diccionario = {
            empresa_desarrolladora: f"[Negative = {emp.iloc[0, 1]}, Neutral = {emp.iloc[0, 2]}, Positive = {emp.iloc[0, 3]}]"
        }

        return diccionario
    except IndexError:
        # Capturar la excepción si no se encuentra la desarrolladora
        mensaje_error = f'No se encontró la desarrolladora {empresa_desarrolladora} en la consulta'
        return mensaje_error

    


#Funcion 6:
def recomendacion_juego(id: int):
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
    Consulta6 = pd.read_csv('Consultas/Consulta6.csv')

    if id in Consulta6['id'].tolist():
        # Obtener la lista de recomendaciones para el juego con el ID proporcionado
        lista = Consulta6['recomendaciones'][Consulta6['id'] == id].iloc[0]
        return lista
    else:
        # Si el ID no se encuentra en la consulta, devolver un mensaje de error
        return 'El id no se ha encontrado'
