from fastapi import APIRouter, FastAPI
from routers import users

app = FastAPI

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})

# uvicorn main:app --reload
# uvicorn users_prova:app --reload
# uvicorn products_prova:app --reload

# uvicorn userjson:app --reload

products_list =  ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def usersjson():
    return products_list

@router.get("/{id}")
async def products_prova(id:int):
    return products_list[id]

@router.get("routers/users")
async def users():
    return products_list
