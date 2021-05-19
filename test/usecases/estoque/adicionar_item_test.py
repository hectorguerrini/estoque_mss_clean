import pytest

from pydantic import ValidationError
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock
from src.usecases.estoque.adicionar_item import AdicionarItem


class Test_adicionar_item():
    def test_adicionar_item(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        addItem = AdicionarItem(repository=repository)
        item = {"nome": "Produto 1", "descricao": "Produto ok",
                "quantidade": 50, "marca": "Butanvac", "vencimento": "2022-04-07"}
        response = addItem.adicionar_item(item)
        assert response.nome == item['nome']
        assert response.descricao == item['descricao']
        assert response.quantidade == item['quantidade']
        assert response.marca == item['marca']
        assert response.vencimento.isoformat() == item['vencimento']

    def test_adicionar_item_error_no_repository(self):
        with pytest.raises(ValidationError):
            AdicionarItem()

    def test_adicionar_item_error_item(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        addItem = AdicionarItem(repository=repository)
        item = {}
        with pytest.raises(KeyError):
            addItem.adicionar_item(item)

    def test_adicionar_item_error_item_quantidade_negative(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        addItem = AdicionarItem(repository=repository)
        item = {"nome": "Produto 1", "descricao": "Produto ok",
                "quantidade": -1, "marca": "Butanvac", "vencimento": "2022-04-07"}
        with pytest.raises(ValidationError) as error_info:
            addItem.adicionar_item(item)
        assert error_info.value.errors() == [{'loc': ('quantidade',),
                                              'msg': 'Quantidade is negative', 'type': 'value_error'}]
