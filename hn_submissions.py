from operator import itemgetter
from urllib import response
import requests

#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"状态码:{r.status_code}")
#将响应的对象转换为python列表
submission_ids = r.json()
#告知列表长度
print(f"列表长度:{len(submission_ids)}")

submission_dicts = []
for submission_id in submission_ids[:30]:
    #对每篇文章都执行一个api调用
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"ID:{submission_id} 状态码:{r.status_code}")
    response_dict = r.json()

    #对于每篇文章都创建一个字典
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"Discussion Link:{submission_dict['hn_link']}")
    print(f"Comments:{submission_dict['comments']}")