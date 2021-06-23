
from src.entities.item.item import ItemModel
from src.external.mongo.config.mongo_config import itensCollection
from src.usecases.ports.estoque_repository_interface import IEstoqueRepository


class EstoqueRepositoryMongo(IEstoqueRepository):
    def listarItens(self):
        lista = []
        for i in itensCollection.find():
            lista.append(ItemModel.make_item_from_dict(i))
        return lista

    def adicionarItens(self, item: ItemModel):
        itensCollection.insert_one(item.toMongo())
