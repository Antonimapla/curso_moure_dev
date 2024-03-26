from fastapi import FastAPI

app = FastAPI()

# Url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastAPI!"


# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/python"} 

#inicia el server: uvicorn main:app --reload
#detener el servidor: CTRL+C

#documentacion con Swagger: http://127.0.0.1:8000/docs
#documentacion con Redocly: http://127.0.0.1:8000/redoc