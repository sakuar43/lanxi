from flask import Flask#导入Flask模块
app=Flask(__name__)#创建Flask对象app
@app.route("/")#装饰器，定义目录为”/“的操作
def hello():#定义函数，遇到网址目录为”/“的执行操作
    return '''Hello world'''
if __name__=="__main__":#文件作为脚本直接执行
    app.run()#运行程序