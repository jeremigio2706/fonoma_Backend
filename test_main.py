from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_total_revenue():
    # Prueba para el endpoint /solution
    payload = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
            {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
            {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"},
        ],
        "criterion": "completed"
    }
    response = client.post("/solution", json=payload)
    assert response.status_code == 200
    assert response.json() == {"total_revenue": 1299.69}
