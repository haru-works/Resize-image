# 画像をリサイズするスクリプト
画像を任意のサイズにリサイズするPythonスクリプトです。

### 利用ライブラリ
 glob  
 Pillow(PIL)  
 argparse   
 datetime  
 os  

### 使い方
```
python resize_images.py --input input_dir --output output_dir --h 320 --w 680
```

| 引数    　| 説明                    　　 |
|----------|-----------------------------|
| --input  | 入力フォルダ（リサイズ元）    |
| --output | 出力フォルダ（リサイズ先）    |
| --h      | リサイズする高さ             |
| --w      | リサイズする幅            　 |
