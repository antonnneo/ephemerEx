FROM python:3.12
LABEL maintainer="antonnneo"

WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install -r requirements.txt

CMD ["sh", "-c", "python3 /app/main.py"]
