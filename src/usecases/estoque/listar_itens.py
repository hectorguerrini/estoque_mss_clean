from pydantic import BaseModel, validator
from src.usecases.ports.estoque_repository_interface import IEstoqueRepository


class ListarItens(BaseModel):
    repository: IEstoqueRepository

    class Config:
        arbitrary_types_allowed = True

    @validator('repository')
    def repository_is_null(cls, v):
        return v

    def listar_itens(self):
        lista = self.repository.listarItens()
        return lista
