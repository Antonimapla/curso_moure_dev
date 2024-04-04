from fastapi import FastAPI
from routers import products, users

app = FastAPI()

#routers
app.include_router(products.router)

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastAPI!"


# Url local: http://127.0.0.1:8000/url

@app.get("/url/")
async def url():
    return {"url":"https://mouredev.com/python"} 

#inicia el server: uvicorn main:app --reload
#detener el servidor: CTRL+C

#uvicorn users:app --reload

#documentacion con Swagger: http://127.0.0.1:8000/docs
#documentacion con Redocly: http://127.0.0.1:8000/redoc
