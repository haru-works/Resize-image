import os
from glob import glob
from PIL import Image
import argparse
import datetime

#現在時間取得用
dt_now = datetime.datetime.now()

#------------------------------------------------------------------------
# 画像リサイズ処理
#------------------------------------------------------------------------
def resize_images(images_dir, image_save_dir, image_size_h,image_size_w):

    # 保存先フォルダ生成
    os.makedirs(image_save_dir, exist_ok=True)
    # 画像ファイルパス読込
    img_paths = glob(os.path.join(images_dir, '*.png'))

    # 画像ファイルパスループ
    for img_path in img_paths:
        # 画像オープン
        image = Image.open(img_path)
        # RGB変換
        rgb_im = image.convert('RGB')

        # オリジナル画像サイズ取得
        iw, ih = image.size
        # リサイズサイズ取得
        w, h = (image_size_w,image_size_h)
        # 倍率設定
        scale = min(w/iw, h/ih)
        # リサイズサイズ再計算
        nw = int(iw*scale)
        nh = int(ih*scale)

        # リサイズ実行
        rgb_im = rgb_im.resize((nw,nh), Image.BICUBIC)

        # 背景生成
        back_im = Image.new("RGB", (image_size_w,image_size_h), color=(128,128,128))
        back_im.paste(rgb_im, ((w-nw)//2, (h-nh)//2))

        # 保存用パス生成＆保存
        save_path = os.path.join(image_save_dir, os.path.basename(img_path))
        end_index = save_path.rfind('.')
        save_path = save_path[0:end_index] + "_" + dt_now.strftime('%Y%m%d%H%M%S') + '.png'
        print('save',save_path)
        back_im.save(save_path,format='PNG')

#------------------------------------------------------------------------
# メイン処理
#------------------------------------------------------------------------
def _main():
    # 引数指定
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--input', type=str,
        help='path to images_dir'
    )
    
    parser.add_argument(
        '--output', type=str,
        help='path to resize_dir '
    )
    
    parser.add_argument(
        '--h', type=int,
        help='resize height'
    )
        
    parser.add_argument(
        '--w', type=int,
        help='resize witdh'
    )
    
    ARGS = parser.parse_args()
    
    #入力ディレクトリ
    images_dir = ARGS.input
    
    #出力ディレクトリ
    image_save_dir = ARGS.output
    
    # ディレクトリが存在しない場合、ディレクトリを作成する  
    if not os.path.exists(image_save_dir):
        os.mkdir(image_save_dir)

    # リサイズサイズ設定
    image_size_h = ARGS.h
    image_size_w = ARGS.w

    # 処理実行
    resize_images(images_dir=images_dir, image_save_dir=image_save_dir,image_size_h=image_size_h,image_size_w=image_size_w)

if __name__ == '__main__':
    _main()
