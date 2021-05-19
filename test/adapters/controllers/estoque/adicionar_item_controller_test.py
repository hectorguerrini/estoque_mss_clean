import pytest

from pydantic import ValidationError

from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock
from src.usecases.estoque.adicionar_item import AdicionarItem
from src.adapters.controllers.estoque.adicionar_item_controller import AdicionarItemController
from src.adapters.controllers.ports.http import HttpRequest


class Test_adicionar_item_controller():

    def test_make_controller_error(self):
        with pytest.raises(ValidationError):
            AdicionarItemController()

    @pytest.mark.asyncio
    async def test_make_controller_handle_ok(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        usecase = AdicionarItem(repository=repository)
        controller = AdicionarItemController(addItem=usecase)
        item = {"nome": "Produto 1", "descricao": "Produto ok",
                "quantidade": 50, "marca": "Butanvac", "vencimento": "2022-04-07"}
        response = await controller.handle(HttpRequest(body=item))
        assert response.statusCode == 200
        assert len(repository.estoque) > 0

    @pytest.mark.asyncio
    async def test_make_controller_handle_badrequest(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        usecase = AdicionarItem(repository=repository)
        controller = AdicionarItemController(addItem=usecase)
        response = await controller.handle(HttpRequest())
        assert response.statusCode == 400
        assert response.body == {"err": "Missing data in body"}

    @pytest.mark.asyncio
    async def test_make_controller_handle_badrequest_key_error(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        usecase = AdicionarItem(repository=repository)
        controller = AdicionarItemController(addItem=usecase)
        response = await controller.handle(HttpRequest(body={}))
        assert response.statusCode == 400
        assert response.body == {"err": "Missing data in body"}

    @pytest.mark.asyncio
    async def test_make_controller_handle_badrequest_validation(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        usecase = AdicionarItem(repository=repository)
        controller = AdicionarItemController(addItem=usecase)
        item = {"nome": "Produto 1", "descricao": "Produto ok",
                "quantidade": -1, "marca": "Butanvac", "vencimento": "2022-04-07"}
        response = await controller.handle(HttpRequest(body=item))
        assert response.statusCode == 400
        assert response.body == {
            "err": "1 validation error for ItemModel\nquantidade\n  Quantidade is negative (type=value_error)"}
