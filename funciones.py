import pandas as pd

#------Funciones:


#Funcion 1:
def PlayTimeGenre(genero: str):
    Consulta1=pd.read_csv('Consultas/Consulta1.csv')
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
        Consulta2=pd.read_csv('Consultas/Consulta2.csv')
        #En caso que la entrada no sea un genero
        if genero not in ['Action', 'Casual', 'Indie', 'Simulation', 'Strategy', 'Free to Play', 'RPG', 'Sports', 'Adventure', 'Racing', 'Early Access', 'Massively Multiplayer', 'Animation & Modeling', 'Video Production', 'Utilities', 'Web Publishing', 'Education', 'Software Training', 'Design & Illustration', 'Audio Production', 'Photo Editing']:
            # Si no está en la lista, lanza una excepción
            return (f"No se encontró el género '{genero}' en la consulta." \
                "\n Lista de Generos: 'Action', 'Casual', 'Indie', 'Simulation', 'Strategy', 'Free to Play', 'RPG', 'Sports', 'Adventure', 'Racing', 'Early Access', 'Massively Multiplayer', 'Animation & Modeling', 'Video Production', 'Utilities', 'Web Publishing', 'Education', 'Software Training', 'Design & Illustration', 'Audio Production', 'Photo Editing'"
            )
        resultado = Consulta2['respuesta'][Consulta2['genero'] == genero]
        return resultado.iloc[0]



#Funcion 3:   
def UsersRecommend(año: int):
    Consulta3=pd.read_csv('Consultas/Consulta3.csv')
    if año < Consulta3['año'].min() or año > Consulta3['año'].max():
        return {"Año no encontrado en el conjunto de datos"}
    # Filtramos para el año de interes
    filtered_df = Consulta3[Consulta3['año'] == año]

    # Seleccionar las 3 desarrolladoras con más revisiones positivas
    filtered_df = Consulta3[Consulta3['año'] == año]
    filtered_df=filtered_df.value_counts('app_name').head(3)
    top=filtered_df.index
    lista=[]
    for i, row in enumerate(top):
        lista.append({f"Puesto {i+1}":row})
    return lista



#Funcion 4:
def UsersWorstDeveloper(año: int):
    Consulta4=pd.read_csv('Consultas/Consulta4.csv')
    if año < Consulta4['año'].min() or año > Consulta4['año'].max():
        return {"Año no encontrado en el conjunto de datos"}
    
    # Filtramos para el año de interes
    filtered_df = Consulta4[Consulta4['año'] == año]

    filtered_df=filtered_df.value_counts('developer').head(3)
    top_worst=filtered_df.index
    lista=[]
    count=1
    for row in top_worst:
        lista.append({f"Puesto {count}":row})
        count+=1
    return lista



#Funcion 5:
def sentiment_analysis(empresa_desarrolladora : str):
    Consulta5=pd.read_csv('Consultas/Consulta5.csv')
    try:
        emp = Consulta5[Consulta5['developer'] == empresa_desarrolladora]
        diccionario = {empresa_desarrolladora: f"[Negative = {emp.iloc[0, 1]}, Neutral = {emp.iloc[0, 2]}, Positive = {emp.iloc[0, 3]}]"}
        return diccionario
    except IndexError:
    # Capturar la excepción si no se encuentra la desarolladora
        mensaje_error = f'No se encontró la desarrolladora {empresa_desarrolladora} en la consulta'
        return mensaje_error
    


#Funcion 6:
def recomendacion_juego(id: int):
    Consulta6=pd.read_csv('Consultas/Consulta6.csv')
    if id in Consulta6['id'].to_list():
        lista=Consulta6['recomendaciones'][Consulta6['id']==id].iloc[0]
        return lista
    else:
        return 'El id no se ha encontrado'