# Auto Downloader

このプログラムは、指定されたURLを現在時刻から1分後に開始し、その後指定された間隔（分）で自動的にダウンロードするためのPythonスクリプトです。`torsocks`を使用してTorネットワーク経由で`wget`コマンドを実行し、ダウンロードが成功した場合にのみ結果を保存します。

## 特徴
- 指定されたURLを定期的にダウンロード
- `torsocks`を使用してTorネットワーク経由でダウンロード
- ダウンロードが成功した場合のみ結果を保存
- ダウンロードの間隔を分単位で指定可能

## 必要なパッケージ
以下のコマンドで必要なパッケージをインストールできます。
```bash
pip install schedule python-crontab
```

##使い方
このリポジトリをクローンまたはダウンロードします。
ターミナルで以下のコマンドを実行します。
```bash
python auto_downloader.py -u <URL> -t <INTERVAL>
```
<URL>：ダウンロードしたいURL
<INTERVAL>：ダウンロードの間隔（分）
例：URLがhttp://example.comで10分おきにダウンロードする場合：
```
python auto_downloader.py -u http://example.com -t 10
```

注意事項
このプログラムはTorネットワークを使用します。使用法と法的側面について理解してからご利用ください。
wgetとtorsocksがインストールされている必要があります。
