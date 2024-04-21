# ベースとなるDockerイメージを指定
FROM balenalib/raspberrypi5-debian-python

# パッケージを更新
RUN apt-get update

# Nginxをインストール
RUN apt-get install -y nginx
# 小規模PJ向けのAPpサーバーであるGunicornをインストール
RUN pip3 install gunicorn

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
RUN mkdir -p /mnt/share && chmod 777 /mnt/share && mkdir /mnt/share/thumbnail && chmod 777 /mnt/share/thumbnail

# Set the timezone
ENV TZ=Asia/Tokyo

# Nginxとアプリケーションを実行する
## gunicornの-wオプションでワーカー数を指定。ラズパイは4コアなので4に設定
## gunicornの-bオプションでバインドするIPアドレスとポートを指定
## run:appはapp.pyのappオブジェクトを指定
CMD service nginx start && gunicorn -w 4 -b 0.0.0.0:3000 run:app

# コンテナの80番ポート開放
EXPOSE 80
