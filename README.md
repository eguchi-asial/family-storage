# overview

以下の環境下で動かせるGUIファイル管理ツールです。
画像の類似度を計測し、同じファイルのuploadを許可しない機能などを持ってます。

- RaspberryPI5/RaspberryPI OS (Debian12)
- Sambaを入れてNATにし、かつ/mnt/shareをSSDとmountしている
- /mnt/share/に画像をuploadすると、thumbnail下に、500x500で自動でサムネイルが作成される
- 同じ画像をuploadすると自動で削除される(WIP cron予定)
- webサーバにnginx、appサーバにgunicornを起用してます
- nginxのaliasで/assetsは/mnt/shareを参照します
  - ブラウザからはサムネイルなどは `http://xxxx/assets/thubnail/thumbnail_12345.png` などで参照できます

# start

localでdocker擬似RaspberryPIでの開発です。

```
sh rerun.sh
```

RaspberryPIのimageが作成され、:80 => :3000ポートでシステムが起動されます。

```
http://localhost
```

にアクセスしてください。

## TODO

- [x] python/flask dev server構築
- [x] /mnt/shareにupload
- [x] /mnt/shareにある画像ファイル一覧取得してtemplateに渡す
- [x] nginxとgunicornをたてて、/mnt/shareを /assetsで見れるようにする
- [x] サムネイルをクリックしたらオリジナル画像を画面幅いっぱいに見れるようにする
- [x] 同じ画像が/mnt/shareにuploadされたら、定期実行バッチで削除する。/mnt/share/thumbnail/も同様に消す。ファイル名は「thumbnail_」が付くかどうかで後は同じなので。
  - [x] 処理プログラム実装
  - [x] cron登録

## アプリケーション(python/unicorn)再起動

```
pstree -ap | grep gunicorn | head -n 1 | awk -F, '{print $2}' | awk '{print $1}' | xargs kill -HUP
```
