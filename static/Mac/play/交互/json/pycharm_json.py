import json

dic={
    "name":"li",
    "age":18,
    "feature":["高","富","帅"]
}
# result=json.dumps(dic)
# result=json.dumps(dic,indent=4)#indent缩进
# print(result)#转为json

# result_1=json.loads(result)
# print(type(result_2))#转为python

# with open("text.txt","w+",encoding='utf-8') as f:#python数据转换为json并保存到文件中
#     result_2=json.dump(dic,ensure_ascii=False,fp=f)#python数据转换为json并保存到文件中
#     print(f.read())
#     f.close()
# #text.txt/py

with open("text.txt","r+",encoding='utf-8') as f:#从文件中读取json，并转化为python数据
    result_3=json.load(fp=f)#从文件中读取json，并转化为python数据
    print(result_3)
    #第一种
    f.seek(53)
    content = f.read(1)
    print(content)
    #第二种
    print(result_3['feature'][-1])
    f.close()