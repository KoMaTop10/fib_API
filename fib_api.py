from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

#FastAPIの定義
app = FastAPI()


# n番目のフィボナッチ数を返す関数
def fibonacci(n:int):
    
    if n <= 0:
        return 0

    if n == 1 or n == 2:
        return 1
    
    a = 1
    b = 1
    
    for i in range(n-2):
        a,b =b, a + b
    return b


# "/fib/?n=n"でn番目のフィボナッチ数を出力する

@app.get("/fib")
def get_fib(n:int):
    if n < 0:
        raise NegativeException(num=n)
    if n == 0:
        raise ZeroException(num=n)
    
    result = fibonacci(n)
    return {"result": result}


# nが負の整数の時の例外処理

class NegativeException(Exception):
    def __init__(self, num: int):
        self.num = num
        

@app.exception_handler(NegativeException)
def negative_exception_handler(request: Request, exc: NegativeException):
    
    return JSONResponse(
        status_code=400,
        content={
            "Status":400,
            "ErrorType":"Negative Number Error",
            "Message":f"{exc.num} is negative number. type natural number"
            },
    )

# n = 0の時の例外処理

class ZeroException(Exception):
    def __init__(self, num: int):
        self.num = num

@app.exception_handler(ZeroException)
def zero_exception_handler(request: Request, exc: ZeroException):
    
    return JSONResponse(
        status_code=400,
        content={
            "Status":400,
            "ErrorType":"Zero Error",
            "Message":"Type natural number"
            },
    )
    

#nの型が異なる場合の例外処理
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    
    return JSONResponse(
        status_code=400,
        content={
            "Status": 400, 
            "ErrorType": "Validation Error",
            "Message":"Type natural number"
            },
    )