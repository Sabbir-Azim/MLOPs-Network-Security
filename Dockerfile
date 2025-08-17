FROM python:3.12.5-alpine3.20

WORKDIR /app
COPY . /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    libcurl \
    curl-dev \
    openssl

RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
