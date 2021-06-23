import pytest
import uuid
from pydantic import ValidationError
from src.entities.item.item import ItemModel


class Test_item():
    def test_make_item(self):
        item = ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                         quantidade=100, marca='Butanvac', vencimento='2022-04-07')
        assert item.nome == 'Produto 1'
        assert item.descricao == 'Produto bom'
        assert item.quantidade == 100
        assert item.marca == 'Butanvac'
        assert item.vencimento.year == 2022

    def test_make_item_from_dict(self):
        json = {"nome": "Produto 1", "descricao": "Produto ok",
                "quantidade": 50, "marca": "Butanvac", "vencimento": "2022-04-07"}
        item = ItemModel.make_item_from_dict(json)
        assert item.nome == 'Produto 1'
        assert item.descricao == 'Produto ok'
        assert item.quantidade == 50
        assert item.marca == 'Butanvac'
        assert item.vencimento.year == 2022

    def test_make_item_with_error_nome(self):
        with pytest.raises(ValidationError) as error_info:
            ItemModel(uuid=uuid.uuid4(), nome='', descricao='Produto bom',
                      quantidade=100, marca='Butanvac', vencimento='2022-04-07')
        assert error_info.value.errors() == [{'loc': ('nome',), 'msg': 'Nome is empty', 'type': 'value_error'}]

    def test_make_item_with_error_marca(self):
        with pytest.raises(ValidationError) as error_info:
            ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                      quantidade=1, marca='', vencimento='2022-04-07')
        assert error_info.value.errors() == [{'loc': ('marca',), 'msg': 'Marca is empty', 'type': 'value_error'}]

    def test_make_item_with_error_quantidade(self):
        with pytest.raises(ValidationError) as error_info:
            ItemModel(uuid=uuid.uuid4(), nome='Produto 1', descricao='Produto bom',
                      quantidade=-1, marca='Butanvac', vencimento='2022-04-07')
        assert error_info.value.errors() == [{'loc': ('quantidade',),
                                              'msg': 'Quantidade is negative', 'type': 'value_error'}]
