from wsgiref import headers
import requests


#执行API调用并储存响应文件
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")
#将API响应赋予给一个变量
response_dict = r.json()#将响应的内容变成字典
#处理结果
#print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")#显示托管的总量
#探索有关项目的信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")
#研究第一个仓库
#repo_dict = repo_dicts[0]
#print(f"\nKeys:{len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
    #print(key)
print("\nSelected information about each repository: ")#打印所有的
for repo_dict in repo_dicts:
    print(f"\nName:{repo_dict['name']}")#项目名称
    print(f"Owner:{repo_dict['owner']['login']}")#项目所有人
    print(f"Stars:{repo_dict['stargazers_count']}")#项目点赞数量、星级
    print(f"Repository:{repo_dict['html_url']}")#项目的链接
    print(f"Created:{repo_dict['created_at']}")#上传时间
    print(f"Updated:{repo_dict['updated_at']}")#最近的更新时间
    print(f"Description:{repo_dict['description']}")#项目描述
