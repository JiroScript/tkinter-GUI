FROM ubuntu:20.04

# タイムゾーンの設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 必要なパッケージのインストール
RUN apt update && apt install -y software-properties-common
RUN apt-get install -y python3 python3-distutils wget
RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && python3 /tmp/get-pip.py
RUN apt-get install -y python3-tk
COPY requirements.txt /tmp/
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /tmp/requirements.txt

# アプリケーションのソースコードをコンテナにコピー
COPY . /app
WORKDIR /app

CMD ["python3", "/app/dawn/scripts/root.py"]

