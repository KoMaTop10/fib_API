from fastapi import FastAPI

app = FastAPI()

def fibonacci(n:int):
    
    if n < 0:
        return -1
    elif n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    
    for i in range(n-2):
        a,b =b, a + b
    return b

@app.get("/fib/{n}")
def index(n:int):
    result = fibonacci(n)
    status = 200
    return {"result": result}