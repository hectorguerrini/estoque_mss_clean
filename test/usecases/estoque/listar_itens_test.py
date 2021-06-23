import pytest
import uuid

from pydantic import ValidationError
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock
from src.usecases.estoque.listar_itens import ListarItens


class Test_listar_itens():
    def test_itens(self):
        listaMock = [
            ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                      quantidade=100, marca='Butanvac', vencimento='2022-04-07'),
            ItemModel(uuid=uuid.uuid4(), nome='Produto 2', descricao='Produto media',
                      quantidade=50, marca='Coronavac', vencimento='2022-02-07'),
            ItemModel(uuid=uuid.uuid4(), nome='Produto 3', descricao='Produto ruim',
                      quantidade=20, marca='AstraFodca', vencimento='2021-12-07')
        ]
        repository = EstoqueRepositoryMock(listaMock)
        listaItens = ListarItens(repository=repository)
        response = listaItens.listar_itens()
        assert len(response) == 3

    def test_listar_itens_error_no_repository(self):
        with pytest.raises(ValidationError):
            ListarItens()
