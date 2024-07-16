FROM python:3.12-slim-bookworm
WORKDIR /opt/app
COPY requirements.txt .
RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install build-essential && \
    apt-get clean && \
    pip install -U pip && \
    pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "./scripts/start-api.sh" ]
