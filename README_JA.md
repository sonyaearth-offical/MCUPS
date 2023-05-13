# MCUPS

english→ [README.md](https://github.com/sonyaearth-offical/backpak/blob/main/README.md)

MCUPSはsonyaEarth(sonyakun)が開発した、Minecraftサーバーのバックアップ機能を提供するCLIソフトウェアです。

## 機能

- サーバーからアクセス可能なローカルディレクトリ (Windowsで言えばCドライブやDドライブのようなもの) へのバックアップ対応
- JSONファイルを使ったバックアップ設定のカスタマイズ
- 直感的で使いやすいコマンドラインインタフェース
- コマンド `pip install .` で簡単にインストール可能
- 環境変数 `BACKPAK_CONFIG` を設定することで、バックアップ設定ファイルへのパスを設定可能

## 使用方法

MCUPSを使用するには、サーバーにPython 3.6以上がインストールされている必要があります。

1. MCUPSリポジトリをクローンしてください。
2. `pip install .` コマンドでMCUPSをインストールしてください。
3. `BACKPAK_CONFIG` 環境変数にバックアップ設定ファイルのパスを設定してください。
4. 次のコマンドでバックアップを実行します: `mcups create [config_number]`。`[config_number]`には、バックアップ設定ファイル内のバックアップ設定の番号を入力してください。

## 近い将来の予定

現在、MCUPSはローカルディレクトリへのバックアップにのみ対応しています。近い将来、FTP/SFTPサーバーへのバックアップ対応を予定しています。
