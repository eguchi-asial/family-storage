# start

```
docker build -t family-storage .
docker run --name family-storage -p 80:3000 -v $(pwd):/app -d family-storage
```

## TODO

- [x] python/flask dev server構築
- [x] /mnt/shareにupload
- [x] /mnt/shareにある画像ファイル一覧取得してtemplateに渡す
- [x] nginxとgunicornをたてて、/mnt/shareを /assetsで見れるようにする
