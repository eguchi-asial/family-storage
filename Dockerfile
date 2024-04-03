# ベースとなるDockerイメージを指定
FROM balenalib/raspberrypi5-debian-python

# パッケージを更新
RUN apt-get update

# ワーキングディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# アプリケーションのソースをコピー
COPY . .

# /mnt/shareディレクトリを作成し、パーミッションを設定
RUN mkdir -p /mnt/share && chmod 777 /mnt/share

# アプリケーションを実行するコマンド
CMD ["python3", "app.py"]

# コンテナの3000番ポートを開放
EXPOSE 3000