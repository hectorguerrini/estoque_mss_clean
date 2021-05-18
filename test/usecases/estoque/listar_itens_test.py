import pytest
import uuid

from pydantic import ValidationError
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock
from src.usecases.estoque.listar_itens import ListarItens


class Test_listar_itens():
    def test_itens(self):
        listaMock = [
            ItemModel(uid=uuid.uuid4(),nome='Produto 1', descricao='Produto bom',quantidade=100),
            ItemModel(uid=uuid.uuid4(),nome='Produto 2', descricao='Produto media',quantidade=50),
            ItemModel(uid=uuid.uuid4(),nome='Produto 3', descricao='Produto ruim',quantidade=20)
        ]
        repository = EstoqueRepositoryMock(listaMock)
        listaItens = ListarItens(repository=repository)
        response = listaItens.listar_itens()
        assert len(response) == 3        

    def test_listar_itens_error_no_repository(self):
        with pytest.raises(ValidationError) as error_info:
             listaItens = ListarItens()
 