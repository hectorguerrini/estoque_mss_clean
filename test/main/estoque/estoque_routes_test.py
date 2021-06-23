from fastapi.testclient import TestClient
from src.main.server import app

client = TestClient(app)


def test_read_itens_estoque():
    response = client.get("/estoque")
    print(response.json())
    assert response.status_code == 200


def test_create_item_estoque():
    item = {"nome": "Produto UNITTEST", "descricao": "UNITTEST DESC",
            "quantidade": 999, "marca": "Butanvac", "vencimento": "2022-04-07"}
    response = client.post("/estoque/item", json=item)
    assert response.status_code == 200
