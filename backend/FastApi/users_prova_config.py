from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

#inicia el server : uvicorn users:app --reload
#inicia el server : uvicorn main:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="moure", url="https://moure.dev", age=35), 
            User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
            User(id=3, name="Haakon", surname="Dahlberg", url="https://Haakon.com", age=33)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com" ,"age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://Haakon.com", "age": 33}]



@app.get("/users/")
async def users():
    return users_list


@app.get("/user/{id}")          #path
async def user(id: int):
    return search_user(id)
    
    
@app.get("/user/")             #query
async def user(id: int):
    return search_user(id)
            
@app.post("/user/", status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        return HTTPException(status_code=204, detail="el usuario ya existe")    
        #return {"error": "el usuario ya existe"}
    else:
        users_list.append(user) 
    return user
        
@app.put("/user/")
async def user(user:User):  
    
    found = False   
    
    for index. saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "no se ha actualizado el usuario"}
    else:
        return user

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado el usuario"}
    

@app.delete("/user/{id}")          #path
async def user(id: int):
    
    found = False
    
    for index. saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True

    if not found:
        return {"error": "no se ha eliminado el usuario"}