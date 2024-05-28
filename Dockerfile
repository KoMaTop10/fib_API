FROM python:3.11.9-slim

WORKDIR root
COPY ./requirements.txt . 

RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip


COPY ./fib_api.py .
COPY sample.html .
RUN pip install -r requirements.txt

CMD ["uvicorn","fib_api:app","--host=0.0.0.0"]
