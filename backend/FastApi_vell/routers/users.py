from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

 
router = APIRouter()
                                                    #esta software accede a un server virtual en localhost(uvicorn)
#inicia el server : uvicorn routers/users:app --reload      #tenemos que ejecutar esta linea desde el terminal para acceder a \users
#inicia el server : uvicorn main:app --reload       # o esta otra si queremos acceder a \main

# Entidad user

class User(BaseModel):          #usamos basemodel para validar los atributos de la clase
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="moure", url="https://moure.dev", age=35),       #creamos una lista de usuarios de la clase User
            User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),
            User(id=3, name="Haakon", surname="Dahlberg", url="https://Haakon.com", age=33)]

@router.get("/usersjson")      #accedemos al directorio \usersjson de localhost 127.0.0.1:8000/usersjson
async def usersjson():      #accedemos mediante una funcion asyncrona
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev", "age": 35},       #nos devuelve la lista de usuarios
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com" ,"age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://Haakon.com", "age": 33}]



@router.get("/users")
async def users():
    return users_list


@router.get("/user/{id}")          #path, accedemos a user a traves del id en la linea de path (get)
async def user(id: int):
    return search_user(id)
    
    
@router.get("/user/")             #query
async def user(id: int):
    return search_user(id)
            
@router.post("/user/", status_code=201)        #codigo de error por defecto. Creamos un nuevo usuario(post)
async def user(user:User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="el usuario ya existe")         #lanza la excepcion 
        #return {"error": "el usuario ya existe"}
    else:
        users_list.append(user) 
    return user
        
@router.put("/user/")
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
    

@router.delete("/user/{id}")          #path
async def user(id: int):
    
    found = False
    
    for index. saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index] 
            found = True

    if not found:
        return {"error": "no se ha eliminado el usuario"}