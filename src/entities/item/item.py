from datetime import date
from pydantic import BaseModel, validator
from uuid import UUID, uuid4
from typing import Optional


class ItemModel(BaseModel):
    uid: Optional[UUID]
    nome: str
    descricao: str = ''
    quantidade: int
    marca: str
    vencimento: date

    @staticmethod
    def make_item_from_dict(dict):
        return ItemModel(uid=uuid4(
        ), nome=dict['nome'], descricao=dict['descricao'], quantidade=dict['quantidade'],marca=dict['marca'],vencimento=dict['vencimento'])

    @validator('nome')
    def nome_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Nome is empty')
        return v.title()
    @validator('marca')
    def marca_is_not_empty(cls, v):
        if len(v) == 0:
            raise ValueError('Marca is empty')
        return v.title()

    @validator('quantidade')
    def quantidade_is_negative(cls, v):
        if v < 0:
            raise ValueError('Quantidade is negative')
        return v
