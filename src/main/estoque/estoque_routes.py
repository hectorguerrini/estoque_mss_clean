

from fastapi import APIRouter
from pydantic import BaseModel
from src.main.estoque.factories.make_controllers import listarItens
from src.entities.item.item import ItemModel

router = APIRouter(
    prefix='/estoque',
    tags=['estoque'],
     responses={404: {"description": "Not found"}},
)
@router.get('/', response_model=list[ItemModel])
async def read_itens_estoque():
    response = listarItens.handle()
    return response.body

