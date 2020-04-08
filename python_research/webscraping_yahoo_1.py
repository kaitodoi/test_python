import requests
#Requestsは基本的にWebページを取得して、そのWebページを解析するためのライブラリ
r = requests.get('https://news.yahoo.co.jp')
#get()関数でURLを指定 rにその情報を格納する
print(r.headers)
print("--------")
print(r.encoding)
print(r.content)
