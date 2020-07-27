import requests
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 第一部分（https://api.github.com/）将请求发送到GitHub网站中响应API调用的部分；
# 接下来的一部分（search/repositories）让API搜索GitHub上的所有仓库。
# repositories后面的问号指出我们要传递一个实参。
# q表示查询，而等号让我们能够开始指定查询（q=）。
# 通过使用language:python，我们指出只想获取主要语言为Python的仓库的信息。
# 最后一部分（&sort=stars）指定将项目按其获得的星级进行排序。
r = requests.get(url)# 遇事不决dir
# print(dir(r))# 遇事不决dir
print("Status code:", r.status_code)
response_dict = r.json()# 将API响应存储在一个变量中，格式json
print(response_dict.keys())# 处理结果
print('total_count：',response_dict["total_count"])

# https://api.github.com/rate_limit  监视API的速率限制

repo_dicts = response_dict['items']# 探索有关仓库的信息
# print(type(repo_dicts))
print("Repositories returned:", len(repo_dicts))


# 研究第一个仓库￼ 
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])# GitHub上星级最高的Python项目
print('Owner:', repo_dict['owner']['login'])# 所有者为用户
print('Stars:', repo_dict['stargazers_count'])# 有***多个GitHub用户给这个项目加星
print('Repository:', repo_dict['html_url'])# 这个项目的仓库的URL
print('Created:', repo_dict['created_at'])# 其创建时间为
print('Updated:', repo_dict['updated_at'])# 最近更新
print('Description:', repo_dict['description'])# 最后，描述指出HTTPie用于帮助从终端执行HTTP调用（CLI是命令行界面的缩写）。