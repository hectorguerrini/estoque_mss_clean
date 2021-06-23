import uuid
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_interface import IEstoqueRepository


class EstoqueRepositoryMock(IEstoqueRepository):
    estoque: list[ItemModel] = [
        ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                  quantidade=100, marca='Butanvac', vencimento='2022-04-07'),
        ItemModel(uuid=uuid.uuid4(), nome='Produto 2', descricao='Produto media',
                  quantidade=50, marca='Coronavac', vencimento='2022-02-07'),
    ]

    def __init__(self, estoque):
        if(estoque is not None):
            self.estoque = estoque

    def listarItens(self):
        return self.estoque

    def adicionarItens(self, item):
        self.estoque.append(item)
