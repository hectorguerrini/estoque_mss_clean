from abc import ABC, abstractmethod
from src.entities.item.item import ItemModel


class IEstoqueRepository(ABC):
    @abstractmethod
    def listarItens(self):
        return

    @abstractmethod
    def adicionarItens(self, itemModel: ItemModel):
        return
