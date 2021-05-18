from fastapi.testclient import TestClient
from src.main.server import app
from uuid import uuid4
client = TestClient(app)

def test_read_itens_estoque():
    response = client.get("/estoque")
    print(response.json())
    assert response.status_code == 200    

def test_create_item_estoque():
    item = {"nome": "Produto 1", "descricao": "Produto ok", "quantidade": 50,"marca": "Butanvac", "vencimento":"2022-04-07"}
    response = client.post("/estoque/item",json=item)    
    assert response.status_code == 200
    