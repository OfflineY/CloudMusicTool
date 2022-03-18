'''
Powered By YUANYUBO
Last Build in 2022

Version: 1.2.0
License: MIT
Github: https://github.com/Offline2008/Cloud-Music-Tool

'''
# GUI 库
import tkinter
import tkinter.messagebox
# 处理官方 Api 返回数据
from urllib.request import urlopen
import json
import jsonpath
# 操作 CMD
import os

# 初始化界面Tk()
app = tkinter.Tk()
# 设置窗口标题
app.title("Version: 1.2.0")
# 修改窗体背景色
app.configure(bg="#272727")
# 修改窗体图标
# app.iconbitmap("https://yuanyubo-studio.vercel.app/favicon.ico")
# 设置窗口大小与左上锚点定位
app.geometry("300x400")
# 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
app.resizable(width=False, height=False)

# 打印 LOGO ，由 http://patorjk.com/software/taag 生成
print("   _____ _                 _ __  __           _   _______          _ ")
print("  / ____| |               | |  \\/  |         (_) |__   __|        | |")
print(" | |    | | ___  _   _  __| | \\  / |_   _ ___ _  ___| | ___   ___ | |")
print(" | |    | |/ _ \\| | | |/ _` | |\\/| | | | / __| |/ __| |/ _ \\ / _ \\| |")
print(" | |____| | (_) | |_| | (_| | |  | | |_| \\__ \\ | (__| | (_) | (_) | |")
print("  \\_____|_|\\___/ \\__,_|\\__,_|_|  |_|\\__,_|___/_|\\___|_|\\___/ \\___/|_|")

# 初始化
print("[INFO] 开始初始化...")

# GET
def get():
    print("[INFO] ---开始---")
    id = data.get()
    # 验证输入是否为空
    if id == "":
        # 是 弹出提示
        tkinter.messagebox.showerror('错误','(ERROR)\n输入框不能为空！')
        print("[ERROR] 输入框为空")
        print("[INFO] ---结束---")
        # 结束进程
    else:
        # 否 继续运行
        # 验证是否为 9 位数
        if id > "100000000":
            # 是 继续运行
            print("[INFO] 获取输入：%s"% (id))
            # 拼接官方 Api 链接
            url = 'https://music.163.com/api/song/enhance/player/url?id=%s&ids=[%s]&br=3200000' % (id, id)
            print("[INFO] 拼接链接：%s"% (url))
            # 请求 JSON 数据
            response = urlopen(url)
            # 取出json文件里的内容，返回的格式是字符串
            html = response.read()
            # 把json形式的字符串转换成python形式的Unicode字符串
            unicodestr = json.loads(html)
            # python形式的列表
            dataurl = jsonpath.jsonpath(unicodestr, "$..url")
            print("[INFO] 获取歌曲DATA：%s" % (dataurl))
            # 判断是否为无效输入
            if dataurl == [None]:
                # 是 提示并结束进程
                tkinter.messagebox.showerror('错误', '(ERROR)\n获取失败，输入内容要为真实内容！\n\n%s' % (unicodestr))
                print("[ERROR] 输入内容不正确导致获取失败")
                print("[INFO] ---结束---")
                # 结束进程
            else:
                # 否 返回数据 继续运行
                a1 = ''.join(dataurl)
                # 发出成功提示
                tkinter.messagebox.showinfo('成功', '获取链接成功：\n%s\n\n点击确定跳转至链接！' % (a1))
                print("[INFO] ---结束---")
                # 使用 CMD 打开链接
                os.system('start %s' % (a1))
                # 获取完成
        else:
            # 否 提示位数不为 9
            tkinter.messagebox.showerror('错误', '(ERROR)\n输入内容要为9位字符！')
            print("[ERROR] 输入框内容小于9位")
            print("[INFO] ---结束---")
            # 结束程序

# GUI
# 极为臃肿，大佬勿看

# 分割线 01
tkinter.Label(app,
              text='___________________________________________________________',
              bg='#272727',
              fg='#000',
              ).place(x='0',y='25')

# 分割线 02
tkinter.Label(app,
              text='___________________________________________________________',
              bg='#272727',
              fg='#000',
              ).place(x='0', y='356')

# 矩形画布
tkinter.Canvas(app,
               width=310,
               height=330,
               bg="#1f1f1f",
               highlightthickness=0
               ).place(x='0', y='44')

# FOTTER 文字
tkinter.Label(app,
              text="Copyright © YuanYuBo. ",
              fg='#555',
              bg='#272727',
              ).place(x=140, y=375)

# TITILE 文字
tkinter.Label(app,
              text="CloudMusic Tool",
              fg='#ccc',
              bg='#272727',
              font=("微软雅黑", 13 , 'bold')
              ).place(x=13, y=7)

# 输入框
data = tkinter.Entry(app,
                bg="#272727",
                fg='#ccc',
                bd='0',
                )
data.place(x=75, y=130)

# 提交按钮
tkinter.Button(app,
               text='点击我跳转至歌曲原文件链接',
               bg='#272727',
               activebackground='#ccc',
               activeforeground='#222',
               fg='#389fef',
               bd='0',
               relief="flat",
               command=get
               ).place(x=65, y=230)

# 提示文字
tkinter.Label(app,
              text="1. 请填写要获取的歌曲 ID，它在每首歌曲\n的链接上可以看到。",
              fg='#ccc',
              bg='#1f1f1f',
              ).place(x=30, y=80)
tkinter.Label(app,
              text="2. 下一步，也是最后一步，点击按钮即可，\n随后将会获取源文件链接地址。",
              fg='#ccc',
              bg='#1f1f1f',
              ).place(x=30, y=180)
tkinter.Label(app,
              text="3. 打开链接，保存即可。注意：暂不支持付费 \n听的歌曲下载。另外请不要用于商业用途。",
              fg='#ccc',
              bg='#1f1f1f',
              ).place(x=30, y=290)

# 页面加载完成提醒
print('[INFO] 初始化完成！')
print('[INFO] 页面内容加载完成！')

# mainloop方法让窗体继续运行，进入事件监听状态
app.mainloop()