from abc import ABC, abstractmethod
from src.entities.item.item import ItemModel


class IEstoqueRepository(ABC):
    @abstractmethod
    def listarItens(self):
        pass

    @abstractmethod
    def adicionarItens(self, itemModel: ItemModel):
        pass
