from fastapi import FastAPI
import os

app = FastAPI()

#app.include_router(products.router)

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/main")
async def main():
    return "¡Hola main FastAPI!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url/")
async def url():
    return {"url":"https://mouredev.com/python"} 

@app.get("/users")
async def user():
    return "Hola user"

@app.get("/users")
async def users():
    return "Hola users prova"

@app.get("/products")
async def products():
    return "Hola products prova"

#inicia el server: uvicorn main:app --reload

# uvicorn main:app --reload

# detener el servidor: CTRL+C

# uvicorn users_prova:app --reload

# uvicorn products:app --reload

#documentacion con Swagger: http://127.0.0.1:8000/docs
#documentacion con Redocly: http://127.0.0.1:8000/redoc
