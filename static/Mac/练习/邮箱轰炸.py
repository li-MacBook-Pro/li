# import smtplib#负责发邮件
# from email.mime.text import MIMEText#制作邮件模版
# from email.utils import formataddr#构建邮箱地址
# #发件人帐号 密码 收件人
# QQ='954957543@qq.com'
# PassWord='Dong0929..'
# user='m17686520521@163.com'#收件人
# def mail():
#     ret=True
#     try:
#         message=MIMEText('<html><h1>如果你喜欢我，我们就一起去旅游吧</h1></html>','html','utf-8')
#         message['form']=formataddr(['我是Anny',QQ])#发件人 昵称 帐号
#         message['To']=formataddr(['小可爱',user])#收件人 昵称 帐号 构建地址 昵称
#         message['subject']='点开邮箱代表你喜欢我，不点开代表我喜欢你'#邮件标题
#         #2、链接SMTP服务器
#         server=smtplib.SMTP_SSL('smtp.qq.com',465)
#         #3、登陆自己的邮箱
#         server.login(QQ,PassWord)#登陆函数  邮箱 密码
#         #4、发送消息
#         server.sendmail(QQ,[user],msg.as_string())#发件人的邮箱 收件人的邮箱 发送邮箱
#     #5、关闭连接
#     except Exception:
#         ret=False#失败
# ret=mail()
#
#
# #以下执行实例需要你本机已安装了支持 SMTP 的服务，如：sendmail。
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['m17686520521@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")




# #如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 第三方 SMTP 服务
# mail_host = "smtp.XXX.com"  # 设置服务器
# mail_user = "XXXX"  # 用户名
# mail_pass = "XXXXXX"  # 口令
#
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")



# #Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中_subtype设置为html。具体代码如下：\
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">这是一个链接</a></p>
# """
# message = MIMEText(mail_msg, 'html', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")



#Python 发送带附件的邮件
#发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
#
# # 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="test.txt"'
# message.attach(att1)
#
# # 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
# message.attach(att2)
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")





#在 HTML 文本中添加图片
#邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加图片的实例如下所示：
# import smtplib
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'from@runoob.com'
# receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# msgRoot = MIMEMultipart('related')
# msgRoot['From'] = Header("菜鸟教程", 'utf-8')
# msgRoot['To'] = Header("测试", 'utf-8')
# subject = 'Python SMTP 邮件测试'
# msgRoot['Subject'] = Header(subject, 'utf-8')
#
# msgAlternative = MIMEMultipart('alternative')
# msgRoot.attach(msgAlternative)
#
# mail_msg = """
# <p>Python 邮件发送测试...</p>
# <p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
# <p>图片演示：</p>
# <p><img src="cid:image1"></p>
# """
# msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
#
# # 指定图片为当前目录
# fp = open('test.png', 'rb')
# msgImage = MIMEImage(fp.read())
# fp.close()
#
# # 定义图片 ID，在 HTML 文本中引用
# msgImage.add_header('Content-ID', '<image1>')
# msgRoot.attach(msgImage)
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, msgRoot.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")



# #使用第三方 SMTP 服务发送
# #这里使用了 QQ 邮箱(你也可以使用 163，Gmail等)的 SMTP 服务，需要做以下配置：
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#
# my_sender = '429240967@qq.com'  # 发件人邮箱账号
# my_pass = 'xxxxxxxxxx'  # 发件人邮箱密码
# my_user = '429240967@qq.com'  # 收件人邮箱账号，我这边发送给自己
#
#
# def mail():
#     ret = True
#     try:
#         msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
#         msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret = False
#     return ret
#
#
# ret = mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")