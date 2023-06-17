from fastapi.testclient import TestClient

from fib_api import app,fibonacci

client = TestClient(app)

def test_read_main():
    result = fibonacci
    response = client.get("/fib",params={"n":99})
    print(response.json)
    assert response.status_code == 200
    
def test_read_main_one():
    result = fibonacci
    response = client.get("/fib",params={"n":1})
    print(response.json)
    assert response.status_code == 200
    
def test_read_main_zero():
    result = fibonacci
    response = client.get("/fib",params={"n":0})
    print(response.json)
    assert response.status_code == 400

def test_read_main_negative():
    result = fibonacci
    response = client.get("/fib",params={"n":-1})
    print(response.json)
    assert response.status_code == 400

def test_read_main_str():
    result = fibonacci
    response = client.get("/fib",params={"n":"test"})
    print(response.json)
    assert response.status_code == 422


