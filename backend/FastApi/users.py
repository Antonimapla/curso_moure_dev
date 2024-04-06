from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:app --reload

#entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id= 1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
        User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
        User(id=3, name="Haakon", surname="Dahlberg", url="https://Haakon.com", age=33)]


@app.get("/usersjson")
async def usersjson():
    return [{ "name":"Brais", "surname":"moure", "url":"https://moure.dev", "age": 35 },
            { "name":"Moure", "surname":"dev", "url":"https://mouredev.com", "age": 35 },
            { "name":"Haakon", "surname":"Dahlberg", "url":"https:/Haakon.com", "age": 33 }]
    
    
@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")      #llamada por path en localhost tenemos que poner /nou/1 (o 2 o 3)
async def users(id: int):
    return search_user(id)

    
# Query
@app.get("/user/")
async def users(id: int):
    return search_user(id)
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"no se ha encontrado el usuario"}
    
    
@app.get("/nou/")               #llamada por query en localhost tenemos que poner /nou/?id=1 (o 2 o 3)
async def users(id: int):
    return search_user(id)







