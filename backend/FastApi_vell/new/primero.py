from fastapi import FastAPI
import os

app = FastAPI()

# inicia el server : uvicorn /new/primero:app --reload
# inicia el server : uvicorn userlist:app --reload
# inicia el server : uvicorn usersjson:app --reload


#entidad user

class User():
    id: int
    name: str
    surname: str
    url: str
    age: int
 
users_list = [User(id=1, name="Brais", surname="moure", url="https://moure.dev", age=34), 
            User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
            User(id=3, name="Haakon", surname="Dahlberg", url="https://Haakon.com", age=33)]   

@app.get("/usersjson")
async def usersjson(usersjson):
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev", "age": 34},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com" ,"age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://Haakon.com", "age": 33}]

@app.get("/")
async def root():
    return "al fin"