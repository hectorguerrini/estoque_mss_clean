import uuid
from src.usecases.estoque.listar_itens import ListarItens
from src.adapters.controllers.estoque.listar_itens_controller import ListarItensController
from src.entities.item.item import ItemModel
from src.usecases.ports.estoque_repository_mock import EstoqueRepositoryMock

listarItens: ListarItensController = (lambda: ListarItensController(listarItens=ListarItens(repository=EstoqueRepositoryMock(None))))()