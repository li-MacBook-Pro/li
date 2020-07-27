import tornado.ioloop
import tornado.web

# 如果出现版本问题，加入此代码
# import platform
#
# if platform.system() == "Windows":
#     import asyncio
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# 满足，当用户在浏览器页面上输入用户密码，点击提交，可以把两个数据提交到后台
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 向浏览器页面写入hello word
        # self.write("Hello, world")
        self.render("ajax.html")#转发，文件名字
    def post(self):
        # 获取前端传入数据，转发文件中name值
        # print(self.get_argument("inp1"))
        # print(self.get_argument("inp2"))
        #         将数据转换为int类型
        inp1=int(self.get_argument("inp1"))
        inp2=int(self.get_argument("inp2"))
        #         求和
        sum=inp1+inp2
        print(sum)
        #         将计算结果返回前端
        # 字典形式fanhui
        result_data={"result":sum}
        self.write(result_data)



if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),#  /和转发文件一致
    ])
    application.listen(8889)# 端口号，都是唯一的。0~65535，建议大了设置。
    tornado.ioloop.IOLoop.current().start()

    # 运行方式1、先运行python文件2、打开浏览器，在地址栏输入：localhost:8888/127.0.0.1:8888