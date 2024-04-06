# family-storageという名前のDockerコンテナを停止
docker stop family-storage

# family-storageという名前のDockerコンテナを削除
docker rm family-storage

# family-storageという名前のDockerイメージを削除
docker rmi family-storage

# family-storageという名前のDockerイメージをビルド
docker build -t family-storage .

# family-storageという名前のDockerコンテナを起動
docker run --name family-storage -p 80:3000 -v $(pwd):/app -d family-storage
