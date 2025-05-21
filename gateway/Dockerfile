FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install fastapi httpx uvicorn
CMD ["uvicorn", "fastapi_gateway:app", "--host", "0.0.0.0", "--port", "8080"]
