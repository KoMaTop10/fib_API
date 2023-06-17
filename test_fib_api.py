from fastapi.testclient import TestClient

from fib_api import app,fibonacci

client = TestClient(app)

def test_read_main():
    result = fibonacci
    response = client.get("/fib",params={"n":11})
    print(response.json)
    assert response.status_code == 200

def test_read_main_negative():
    result = fibonacci
    response = client.get("/fib",params={"n":-1})
    print(response.json)
    assert response.status_code == 400

