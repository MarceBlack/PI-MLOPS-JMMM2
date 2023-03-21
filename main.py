import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenido a mi API de streaming de películas para Henry, te saluda Jorge Marcelo Mendez"}

# Consulta 1: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get("/get_max_duration")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    streaming_ratings_df = pd.read_csv('streaming_ratings.csv')
    
    # Filtrar las columnas
    filtered_df = streaming_ratings_df.loc[(streaming_ratings_df["year"] == year if year is not None else True) &
                         (streaming_ratings_df["platform"] == platform if platform is not None else True) &
                         (streaming_ratings_df["duration_type"] == duration_type if duration_type is not None else True)]

    # Verificar si el DataFrame filtrado está vacío
    if filtered_df.empty:
        return {"message": "No se encontró una película con los filtros proporcionados."}
    
    # Mostrar la película con la mayor duración
    max_duration_movie = filtered_df.loc[filtered_df["duration_int"].idxmax()]

    return max_duration_movie.to_dict()

# Consulta 2: Cantidad de películas por plataforma y filtrar plataforma, score promedio y año indicados
@app.get('/score_count/')
def get_score_count(platform: str, scored: float, year: int = None):
    streaming_ratings_df = pd.read_csv('streaming_ratings.csv')
    # Filtrar los datos según los valores de los parámetros
    filtered = streaming_ratings_df.copy()
    filtered = filtered[filtered['platform'] == platform]
    if year is not None:
        filtered = filtered[filtered['year'] == year]
    
    # Contar la cantidad de películas por plataforma y devolver los resultados
    count = len(filtered[filtered['scored'] > scored])
    return {'count': count}

# Consulta 3: Cantidad de películas por plataforma y filtrar los resultados según la plataforma indicada
@app.get('/count_platform/')
def get_count_platform(platform: str):
    streaming_ratings_df = pd.read_csv('streaming_ratings.csv')
    count = len(streaming_ratings_df[streaming_ratings_df['platform'] == platform])
    return {'count': count}

# Consulta 4: Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get('/actor/')
async def get_actor(platform: str, year: int):
    streaming_ratings_df = pd.read_csv('streaming_ratings.csv')
    # Filtrar por plataforma y año
    df_filtered = streaming_ratings_df[(streaming_ratings_df['platform'] == platform) & (streaming_ratings_df['year'] == year)]
    # Concatenar los valores de la columna "cast"
    actors_df = df_filtered['cast'].str.split(', ', expand=True)
    # Contar la frecuencia de cada actor
    actor_count = actors_df.stack().value_counts().reset_index()
    # Obtener el actor con mayor frecuencia
    most_common_actor = actor_count.iloc[0]['index']
   
    return most_common_actor

