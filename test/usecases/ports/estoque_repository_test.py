import uuid
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock


class Test_estoque_repository():

    def test_make_repository_mock(self):
        listaMock = [
            ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                      quantidade=100, marca='Butanvac', vencimento='2022-04-07'),
            ItemModel(uuid=uuid.uuid4(), nome='Produto 2', descricao='Produto media',
                      quantidade=50, marca='Coronavac', vencimento='2022-02-07'),
            ItemModel(uuid=uuid.uuid4(), nome='Produto 3', descricao='Produto ruim',
                      quantidade=20, marca='AstraFodca', vencimento='2021-12-07')
        ]
        repository = EstoqueRepositoryMock(listaMock)
        lista = repository.listarItens()
        assert lista == listaMock

    def test_add_and_list_itens(self):
        listaMock = []
        repository = EstoqueRepositoryMock(listaMock)
        item = ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                         quantidade=100, marca='Butanvac', vencimento='2022-04-07'),
        repository.adicionarItens(item)
        lista = repository.listarItens()
        assert lista[0] == item

    def test_add_and_list_itens_with_null_param(self):
        repository = EstoqueRepositoryMock(None)
        item = ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                         quantidade=100, marca='Butanvac', vencimento='2022-04-07'),
        repository.adicionarItens(item)
        lista = repository.listarItens()
        assert len(lista) > 0
