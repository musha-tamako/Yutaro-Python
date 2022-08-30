import requests
import os, time


# 保存先のフォルダを指定
save_dir = './renban_image'

# 保存フォルダがなければ作る
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

# 画像のURLを1枚のみ指定
url = 'https://images.usopen.org/ix-events-usta-players/wta315086.jpg'
save_file = save_dir + '/315086.jpg'

# URLのリソースを取得
res = requests.get(url)
print(res.status_code)

# ファイルに保存
with open(save_file, 'wb') as fp:
    fp.write(res.content)
print("save:", save_file)