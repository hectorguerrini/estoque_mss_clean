from fastapi.testclient import TestClient
from src.main.server import app

client = TestClient(app)

def test_read_itens_estoque():
    response = client.get("/estoque")
    print(response.json())
    assert response.status_code == 200    