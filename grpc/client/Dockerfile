FROM python:3.10-slim

WORKDIR /app

COPY client/client.py ./client.py
COPY greet.proto ./greet.proto

RUN pip install grpcio grpcio-tools

CMD ["python", "client.py"]
