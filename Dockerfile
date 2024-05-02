# ベースとなるDockerイメージを指定
FROM balenalib/raspberrypi5-debian-python

# middlewareをinstall
## cronはraspberrypiのimageにはinstallされていないので、installする
RUN apt-get update && apt-get install -y nginx && apt-get install -y cron && apt-get install -y ffmpeg
# 小規模PJ向けのAPpサーバーであるGunicornをインストール
RUN pip3 install gunicorn

# ワーキングディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Nginxの設定ファイルをコピー
COPY nginx.conf /etc/nginx/sites-available/default

# crontaの設定ファイルをコピー
COPY crontab /etc/cron.d/my-crontab
RUN chmod 0644 /etc/cron.d/my-crontab
RUN crontab /etc/cron.d/my-crontab

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
CMD service cron start && service nginx start && gunicorn -w 4 -b 0.0.0.0:3000 run:app

# コンテナの80番ポート開放
EXPOSE 80
