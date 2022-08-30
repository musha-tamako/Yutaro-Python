import requests
import os, time


# 保存先のフォルダを指定
save_dir = './renban_image'
# 画像の基本URLを指定
base_url = 'https://images.usopen.org/ix-events-usta-players/wta315086.jpg'

# 順番に画像をダウンロードして保存する
def download_all():

    # 保存フォルダがなければ作る
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # 1～1000番まで連番で画像をダウンロード
    for id in range(1,1000):
        download_file(id)
        #1秒待ちます。大切。
        time.sleep(1)

# id番目の画像をダウンロードする
def download_file(id):
   
    # 名前は1000番まで
    url = base_url.format(id%1000, id)
    save_file = save_dir + '/' + str(id) + '.jpg'

    # URLのリソースを取得
    res = requests.get(url)
    print(url)

    # URLリソースの取得チェック
    if not res.ok:
        print("失敗:", res.status_code)
        return
    # ファイルに保存
    with open(save_file, 'wb') as fp:
        fp.write(res.content)
    print("save:", save_file)

# メイン処理
if __name__ == '__main__':
    download_all()