FROM mcr.microsoft.com/devcontainers/python:3.12

# 作業ディレクトリ
WORKDIR /workspace

# SQLite3のインストール
RUN apt-get update && apt-get install -y sqlite3

# 必要なライブラリをインストール
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt

COPY . /workspace/