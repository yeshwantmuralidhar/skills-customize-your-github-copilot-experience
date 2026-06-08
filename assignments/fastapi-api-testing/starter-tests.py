from fastapi.testclient import TestClient
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Load app from starter-code.py (hyphenated filename cannot be imported directly).
module_path = Path(__file__).with_name("starter-code.py")
spec = spec_from_file_location("starter_code", module_path)
starter_code = module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(starter_code)

client = TestClient(starter_code.app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_get_items_returns_list():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_valid_id():
    response = client.get("/items/1")
    assert response.status_code == 200
    body = response.json()
    assert "id" in body and "name" in body and "price" in body


def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 404


def test_create_item_invalid_payload():
    response = client.post("/items", json={"name": "Marker"})
    assert response.status_code == 422
