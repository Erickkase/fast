from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

movies = [
    {
        "id": 1,
        "titulo": "Avatar",
        "descripcion": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "año": "2009",
        "ranking": 7.8,
        "categoria": "Acción"
    },
     {
        "id": 2,
        "titulo": "Avatar2",
        "descripcion": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "año": "2022",
        "ranking": 7.8,
        "categoria": "Acción"
    }
]

@app.get("/")
def read_root():
    return {"message": "Hola Mundo"}

@app.get("/home")
def home():
    return movies

@app.get('/movies/{id}', tags =['home'])
def get_movies(id: int):
    for movie in movies:

        if movie['id'] == id:
            return movie
    
    return []




