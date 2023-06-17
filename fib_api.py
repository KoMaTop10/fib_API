from fastapi import FastAPI,HTTPException,Request,Query
from fastapi.responses import JSONResponse

app = FastAPI()

def fibonacci(n:int):
    
    if n <= 0:
        raise HTTPException(status_code=400, detail="Bad request")

    if n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    
    for i in range(n-2):
        a,b =b, a + b
    return b

@app.get("/fib")
def index(n:int=Query()):
    if n < 1:
        raise UnicornException(num=n)
    
    result = fibonacci(n)
    return {"result": result}

class UnicornException(Exception):
    def __init__(self, num: int):
        self.num = num

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=400,
        content={
            "status":400,
            "message":"Bad request"
            },
    )