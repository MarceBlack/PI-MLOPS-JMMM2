# PI-MLOPS-JMMM2
¡Bienvenidos a mi primer proyecto individual! En esta ocasión, me desempeñé en el rol de un MLOps Engineer.


# Proyecto Individual Henry Nº1
### Jorge Marcelo Mendez Mendez



## INTRODUCCION
El proyecto consistía en situarse en el rol de Data Engineer, a quien como miembro del equipo de una empresa, el Tech Lead le solicita realizar un proceso de ETL sobre cuatro datasets proporcionados, conteniendo información relativa a los catálogos de series y películas de cuatro plataformas de streaming (Netflix, Amazon Prime Video, Disney y Hulu).

Asimismo, se solicitó elaborar una API con un framework de FastAPI, a efectos de disponer los datos en línea, bajo cinco consultas predefinidas.

Tambien, se solicitó documentar todo el proceso y el funcionamiento de la API, asi como también, realizar un video a ser remitido al Tech Lead, quien nos encargó el proyecto para que, nos efectúen un feedback sobre el mismo.

# Propuesta de trabajo 
Prodedemos a dividir nuestro proyecto en 3 etapas que se acompaña de su respectivo notebook.

## Transformaciones: 
Para las transformaciones debemos:

> Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los conjuntos de datos (ejemplo para títulos de Amazon = as123)

> Los valores nulos del campo rating deberán reemplazarse por la cadena “G” (corresponde al rating de madurez: “general para todos los públicos”

> De haber fechas, debe tener el formato AAAA-mm-dd

> Los campos de texto deben estar en minúsculas, sin excepciones

> El campo de duración debe convertirse en dos campos: duración_int y duración_tipo. El primero será un entero y el segundo una cadena indicando la unidad de medición de duración: min (minutos) o temporada (temporadas)

Cada uno de estos puntos se los ven desarrollados paso a paso en el notebook llamado: PIMLOPS_ETL.ipynb

## Desarrollo API: Se propone disponibilizar los datos de la empresa usando el framework FastAPI. Las consultas que se proponen son las siguientes:

> Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(año, plataforma, duración_tipo))

> Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

> Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(plataforma))

> Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))

Cada uno de estos puntos se los ven desarrollados paso a paso en el notebook llamado: PIMLOPS_API.ipynb
Tambien, para este paso de Desarrollo de API se acompaña con un archivo "main.py", que basicamente, contiene el codigo para poder generar la API


## Deployment: 
Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas facil😄. Tambien podrias usar Railway, pero ten en cuenta que con este si necesitas dockerizacion.

## Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías, y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Sabes que puedes apoyarte en librerías como pandas, ma

## Sistema de recomendación:

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dio un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendaciones debe ser implementado para tener una interfaz gráfica amigable para ser utilizado, utilizando Gradio para su implementación o bien con alguna solución como Streamlit o algo similar en local (tener el implementación del sistema de recomendaciones o una interfaz gráfica es un plus al proyecto).



#LINK IMPORTANTES

# API

https://pai-ops-jmmmm.onrender.com

# Video de demostración
https://youtu.be/dxuxt3FOlRw

# Links de ayuda y soporte
        
Toda la bibliografía recomendada y provista durante el bootcamp y las clases de todos los días. (Si queres conocer más sobre esto, ingresá acá:

Videos de youtube como:
        
    >   🚀Como crear un Repositorio y Subir Proyecto a 👉GITHUB👈 Paso a Paso💻
    https://www.youtube.com/watch?v=eQMcIGVc8N0&t=370s

    >   https://www.youtube.com/watch?v=_eWEmRWhk9A
    >   https://www.youtube.com/watch?v=2tOhTGBWZXY&list=LL
    >   https://www.youtube.com/watch?v=BvvH3ohis6E

Sitios de internet como:

    >  HX-F Negrete/render-fastapi-tutorial
        https://github.com/HX-FNegrete/render-fastapi-tutorial 
    >   https://www.fastapitutorial.com/blog/fastapi-course/
    >   https://medium.com/dev-jam/docker-in-a-nutshell-f2e315211195
    >   https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/
    >   https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
    >   https://fastapi.tiangolo.com/tutorial/
    >   Deploy FastAPI App to Render
    https://blog.akashrchandran.in/deploying-fastapi-application-to-render
