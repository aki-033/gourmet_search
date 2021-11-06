import requests
import json

from pathlib import Path
import os, environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Environmental variables
env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env')
env.read_env(env_file)
if env('HOTPEPPER_API_KEY'):
    HOTPEPPER_API_KEY = env('HOTPEPPER_API_KEY')
    print(HOTPEPPER_API_KEY)

##### APIのGET先のURL
# r_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
# r_url = "https://webservice.recruit.co.jp/hotpepper/genre/v1/"
# r_url = "http://webservice.recruit.co.jp/hotpepper/large_area/v1/"
# r_url = "http://webservice.recruit.co.jp/hotpepper/middle_area/v1/"
# r_url = "http://webservice.recruit.co.jp/hotpepper/small_area/v1/"

large_area_code = "Z011"

# 中エリア
def get_middle_area():

    r_url = "http://webservice.recruit.co.jp/hotpepper/middle_area/v1/"

    query = {
        "key": HOTPEPPER_API_KEY,
        "large_area": large_area_code,
        #"order": 1,  # 名前の順
        #"count": 100,
        #"start": 0,  # 検索結果の何番目から出力するか
        "format": "json",
    }

    responce = requests.get(r_url, query)
    result = json.loads(responce.text)["results"]["middle_area"]

    return result

# 小エリア
def get_small_area(middle_area):

    r_url = "http://webservice.recruit.co.jp/hotpepper/small_area/v1/"

    query = {
        "key": HOTPEPPER_API_KEY,
        "middle_area": middle_area,
        #"order": 1,  # 名前の順
        #"count": 100,
        #"start": 0,  # 検索結果の何番目から出力するか
        "format": "json",
    }

    responce = requests.get(r_url, query)
    result = json.loads(responce.text)["results"]["small_area"]

    return result

# ジャンル 
def get_genre():

    r_url = "https://webservice.recruit.co.jp/hotpepper/genre/v1/"

    query = {
        "key": HOTPEPPER_API_KEY,
        "format": "json",
    }

    responce = requests.get(r_url, query)
    result = json.loads(responce.text)["results"]["genre"]

    return result

# ショップ
def get_shop(middle_area, small_area, genre):

    r_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"

    query = {
        "key": HOTPEPPER_API_KEY,
        "large_area": large_area_code,
        "middle_area": middle_area,
        "small_area": small_area,
        "genre": genre,
        "count": 3,
        "start": 0,  # 検索結果の何番目から出力するか
        "format": "json",
    }

    responce = requests.get(r_url, query)
    result = json.loads(responce.text)["results"]["shop"]

    return result
