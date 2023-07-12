import tkinter
import tkinter.messagebox
from urllib.request import urlopen
import json
import jsonpath
import os

app = tkinter.Tk()
app.title("Version: 1.2.0")
app.configure(bg="#272727")
app.geometry("300x400")
app.resizable(width=False, height=False)


def get():
    data_id = data.get()
    # 验证输入是否为空
    if data_id == "":
        tkinter.messagebox.showerror('错误', '(ERROR)\n输入框不能为空！')
    else:
        if len(data_id) >= 9:
            url = 'https://music.163.com/api/song/enhance/player/url?id=%s&ids=[%s]&br=3200000' % (data_id, data_id)
            response = urlopen(url)
            html = response.read()
            unicode_str = json.loads(html)
            dataurl = jsonpath.jsonpath(unicode_str, "$..url")
            if dataurl == [None]:
                tkinter.messagebox.showerror('错误', '(ERROR)\n获取失败，输入内容要为真实内容！\n\n%s' % unicode_str)
            else:
                a1 = ''.join(dataurl)
                tkinter.messagebox.showinfo('成功', '获取链接成功：\n%s\n\n点击确定跳转至链接！' % a1)
                print("[INFO] ---结束---")
                # 使用 CMD 打开链接
                os.system('start %s' % a1)
        else:
            tkinter.messagebox.showerror('错误', '(ERROR)\n输入内容要为9位字符！')


tkinter.Label(app, text='___________________________________________________________', bg='#272727', fg='#000')\
    .place(x='0', y='25')
tkinter.Label(app, text='___________________________________________________________', bg='#272727', fg='#000')\
    .place(x='0', y='356')

tkinter.Canvas(app, width=310, height=330, bg="#1f1f1f", highlightthickness=0)\
    .place(x='0', y='44')

tkinter.Label(app, text="Copyright © YuanYuBo. ", fg='#555', bg='#272727')\
    .place(x=140, y=375)

tkinter.Label(app, text="CloudMusic Tool", fg='#ccc', bg='#272727', font=("微软雅黑", 13, 'bold'))\
    .place(x=13, y=7)

data = tkinter.Entry(app, bg="#272727", fg='#ccc', bd='0')
data.place(x=75, y=130)

tkinter.Button(app, text='点击我跳转至歌曲原文件链接', bg='#272727', activebackground='#ccc', activeforeground='#222',
               fg='#389fef', bd='0', relief="flat", command=get)\
    .place(x=65, y=230)

tkinter.Label(app, text="1. 请填写要获取的歌曲 ID，它在每首歌曲\n的链接上可以看到。", fg='#ccc', bg='#1f1f1f')\
    .place(x=30, y=80)
tkinter.Label(app, text="2. 下一步，也是最后一步，点击按钮即可，\n随后将会获取源文件链接地址。", fg='#ccc', bg='#1f1f1f')\
    .place(x=30, y=180)
tkinter.Label(app, text="3. 打开链接，保存即可。注意：暂不支持付费 \n听的歌曲下载。另外请不要用于商业用途。", fg='#ccc', bg='#1f1f1f')\
    .place(x=30, y=290)

app.mainloop()
