from fastapi import APIRouter
from src.main.estoque.factories.make_controllers import listarItens, adicionarItem
from src.entities.item.item import ItemModel
from src.adapters.controllers.ports.http import HttpRequest

router = APIRouter(
    prefix='/estoque',
    tags=['Estoque'],
    responses={404: {"description": "Not found"}},
)


@router.get('/', response_model=list[ItemModel])
async def read_itens_estoque():
    response = await listarItens.handle()
    return response.body


@router.post('/item', response_model=ItemModel)
async def create_item_estoque(item: ItemModel):
    response = await adicionarItem.handle(HttpRequest(body=item.dict()))
    return response.body
