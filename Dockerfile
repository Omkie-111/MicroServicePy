FROM python:3.10.12-slim-buster

RUN mkdir -p /app
COPY . /app/
WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential cmake zlib1g-dev libbrotli-dev liblz4-dev libsnappy-dev libthrift-dev python3-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
