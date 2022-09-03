import requests
import json

#执行API调用并储存响应11111111
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code :{r.status_code}")
#将API响应赋予一个变量
response_dict = r.json()
#探索数据结构
readable_file = 'readable_hn_data.json'
with open(readable_file,"w") as f:
    json.dump(response_dict,f,indent=4)