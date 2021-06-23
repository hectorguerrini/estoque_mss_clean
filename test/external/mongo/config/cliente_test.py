from src.external.mongo.config.mongo_config import client


def test_mongo_cliente_collection():
    client['unittest']['estoque'].insert_one({'teste': 123})


def test_mongo_client_find():
    response = client['unittest']['estoque'].find()
    print(response)
