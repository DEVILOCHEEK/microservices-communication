FROM python:3.10-slim

WORKDIR /app

COPY server/server.py ./server.py
COPY greet.proto ./greet.proto

RUN pip install grpcio grpcio-tools

CMD ["python", "server.py"]
