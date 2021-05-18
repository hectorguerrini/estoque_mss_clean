import pytest
import uuid
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock
from src.usecases.estoque.listar_itens import ListarItens
from src.adapters.controllers.estoque.listar_itens_controller import ListarItensController
class Test_listar_itens_controller():
    def test_make_controller(self):
        listaMock = [
            ItemModel(uid=uuid.uuid4(),nome='Produto 1', descricao='Produto bom',quantidade=100,marca='Butanvac',vencimento='2022-04-07'),
            ItemModel(uid=uuid.uuid4(),nome='Produto 2', descricao='Produto media',quantidade=50,marca='Coronavac',vencimento='2022-02-07'),
            ItemModel(uid=uuid.uuid4(),nome='Produto 3', descricao='Produto ruim',quantidade=20,marca='AstraFodac',vencimento='2022-08-07')
        ]
        repository = EstoqueRepositoryMock(listaMock)
        usecase = ListarItens(repository=repository)
        controller = ListarItensController(listarItens=usecase)
        response = controller.handle()
        assert response.statusCode == 200
        assert response.body == listaMock
        

