from fastapi import FastAPI

app = FastAPI()

# url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "Hola FastApi"


# url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return "Hola url"

@app.get("/new")
async def new():
    return "Hola new"

# uvicorn main:app --reload
# docu swagger: http://127.0.0.1:8000/docs
# docu swagger: http://127.0.0.1:8000/redoc