import pytest
import json
import os

from app import app

@pytest.fixture()
def defapp():
    app.config.update({
        "TESTING": True,
    })
    with open('./water.json', 'w') as f:
        f.write(json.dumps({"water": 70, "adding": []})) 
    yield app

@pytest.fixture()
def client(defapp):
    return defapp.test_client()

# Test pour l'ajout d'eau
def test_add_water(client):
    response = client.get("/add_water")
    result = json.loads(response.data)
    assert result['water'] == 80  

def test_request_example(client):
    response = client.get("/water")
    result = json.loads(response.data)
    assert result['water'] == 70  

def test_add_water_user(client):
    user_id = "123" 
    response = client.get(f"/add_water/{user_id}")
    result = json.loads(response.data)
    assert result['water'] == 80  
