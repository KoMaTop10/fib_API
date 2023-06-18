from fastapi.testclient import TestClient

from fib_api import app

client = TestClient(app)

def test_read_main():
    response = client.get("/fib",params={"n":99})
    assert response.status_code == 200
    assert response.json() == {"result":218922995834555169026}
    
def test_read_main_one():
    response = client.get("/fib",params={"n":1})
    assert response.status_code == 200
    assert response.json() == {"result":1}
    
def test_read_main_zero():
    response = client.get("/fib",params={"n":0})
    assert response.status_code == 400
    assert response.json() == {"Status":400,"ErrorType":"Zero Error","Message":"Type natural number"}

def test_read_main_negative():
    response = client.get("/fib",params={"n":-1})
    assert response.status_code == 400
    assert response.json() == {"Status":400,"ErrorType":"Negative Number Error","Message":"-1 is negative number. type natural number"}
def test_read_main_double():
    response = client.get("/fib",params={"n":3.14})
    assert response.status_code == 400
    assert response.json() == {"Status":400,"ErrorType":"Validation Error","Message":"Type natural number"}
    
def test_read_main_str():
    response = client.get("/fib",params={"n":"test"})
    assert response.status_code == 400
    assert response.json() == {"Status":400,"ErrorType":"Validation Error","Message":"Type natural number"}


