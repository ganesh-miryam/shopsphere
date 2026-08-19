from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_products():
    response = client.get("/products/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_product():
    product = {
        "name": "Test Laptop",
        "description": "Laptop for testing",
        "price": 999.99,
        "quantity": 5
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Laptop"
    assert data["price"] == 999.99
    assert data["quantity"] == 5

    return data["id"]


def test_product_crud_flow():
    product = {
        "name": "CRUD Laptop",
        "description": "Testing complete CRUD flow",
        "price": 799.99,
        "quantity": 10
    }

    # CREATE
    response = client.post("/products/", json=product)
    assert response.status_code == 201

    product_id = response.json()["id"]

    # READ
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "CRUD Laptop"

    # UPDATE
    updated_product = {
        "name": "Updated CRUD Laptop",
        "description": "Updated product",
        "price": 899.99,
        "quantity": 15
    }

    response = client.put(
        f"/products/{product_id}",
        json=updated_product
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated CRUD Laptop"

    # DELETE
    response = client.delete(f"/products/{product_id}")

    assert response.status_code == 200

    # VERIFY DELETE
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 404


def test_product_not_found():
    response = client.get("/products/99999")

    assert response.status_code == 404