# ベースとなるDockerイメージを指定
FROM balenalib/raspberrypi5-debian-python

# パッケージを更新
RUN apt-get update

# Nginxをインストール
RUN apt-get install -y nginx

# ワーキングディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Nginxの設定ファイルをコピー
COPY nginx.conf /etc/nginx/sites-available/default

# アプリケーションのソースをコピー
COPY . .

# /mnt/shareディレクトリを作成し、パーミッションを設定
RUN mkdir -p /mnt/share && chmod 777 /mnt/share

# Nginxとアプリケーションを実行するコマンド
CMD service nginx start && python3 app.py

# コンテナの80番ポート開放
EXPOSE 80
