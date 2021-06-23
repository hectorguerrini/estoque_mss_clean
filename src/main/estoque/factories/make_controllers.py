from src.usecases.estoque.listar_itens import ListarItens
from src.usecases.estoque.adicionar_item import AdicionarItem
from src.adapters.controllers.estoque.listar_itens_controller import ListarItensController
from src.adapters.controllers.estoque.adicionar_item_controller import AdicionarItemController
from src.external.mongo.ports.estoque_repository_mongo import EstoqueRepositoryMongo
# from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock

listarItens: ListarItensController = (lambda: ListarItensController(
    listarItens=ListarItens(repository=EstoqueRepositoryMongo())))()

adicionarItem: AdicionarItemController = (lambda: AdicionarItemController(
    addItem=AdicionarItem(repository=EstoqueRepositoryMongo())))()
