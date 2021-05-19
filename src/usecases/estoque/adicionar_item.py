from typing import Any
from pydantic import BaseModel, validator
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_interface import IEstoqueRepository


class AdicionarItem(BaseModel):
    repository: IEstoqueRepository

    class Config:
        arbitrary_types_allowed = True

    @validator('repository')
    def repository_is_null(cls, v):
        return v

    def adicionar_item(self, item: Any):
        item = ItemModel.make_item_from_dict(item)
        self.repository.adicionarItens(item)
        return item
