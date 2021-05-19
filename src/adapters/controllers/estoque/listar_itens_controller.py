from pydantic import BaseModel, validator, ValidationError
from src.usecases.estoque.listar_itens import ListarItens
from src.adapters.controllers.ports.http import HttpResponse
from src.adapters.controllers.helpers.http_helpers import ok, serverError


class ListarItensController(BaseModel):
    listarItens: ListarItens

    @validator('listarItens')
    def usecase_is_null(cls, v):
        return v

    async def handle(self) -> HttpResponse:
        try:
            response = self.listarItens.listar_itens()
            return ok(response)
        except ValidationError as e:
            print(e)
            return serverError(str(e))
