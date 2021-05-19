from pydantic import BaseModel, validator, ValidationError
from src.usecases.estoque.adicionar_item import AdicionarItem
from src.adapters.controllers.helpers.http_helpers import badRequest, ok
from src.adapters.controllers.ports.http import HttpResponse, HttpRequest


class AdicionarItemController(BaseModel):
    addItem: AdicionarItem

    @validator('addItem')
    def usecase_is_null(cls, v):
        return v

    async def handle(self, req: HttpRequest) -> HttpResponse:
        try:
            if (req.body is None):
                return badRequest('Missing data in body')

            response = self.addItem.adicionar_item(req.body)

            return ok(response)
        except ValidationError as e:
            print(e)
            return badRequest(str(e))
        except KeyError as k:
            print(k)
            return badRequest('Missing data in body')
