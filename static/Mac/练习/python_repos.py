'''import requests
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


# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
'''

'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应￼
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:",r.status_code)
# 将API响应存储在一个变量中￼ 
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# 研究有关仓库的信息￼ 
repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)


chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
'''

# 添加自定义工具提示

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value': repo_dict['stargazers_count'],'label': repo_dict['description'],}
    plot_dicts.append(plot_dict)
# 可视化￼ 
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names



chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# 根据数据绘图
