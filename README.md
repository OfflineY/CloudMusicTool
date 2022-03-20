#  CloudMusicTool

Pyrhon制作的网易云音乐歌曲获取工具，它可以获取网易云音乐在线歌曲的源链接。仅用于**学习与娱乐，请勿商用。**

## 📑 目录
 - [💾下载运行程序](#-下载运行程序)

 - [📗使用工具](#-使用工具)
 
 - [🛠重构](#-重构)
 
 - [🎈技术栈&原理](#-技术栈&原理)

## 💾 下载运行程序

 - Windows 普通版本：[main.exe](https://raw.fastgit.org/Offline2008/Cloud-Music-Tool/main/dist/main.exe)

 - Windows 开发版：[main-dev.exe](https://raw.fastgit.org/Offline2008/Cloud-Music-Tool/main/dist/main-dev.exe)[^1]

## 📗 使用工具
下载完成双击打开，把你的歌曲 ID 填入输入框内然后点击下方按钮，这将会跳转至歌曲原链接，在浏览器打开下载即可。具体信息如图所示。

![](https://gitee.com/offline2008/img/raw/master/Snipaste_2022-03-18_13-20-39.jpg)

## 🛠 重构

1. 首先Clone 整个仓库，需要安装部分组件[^2]，推荐使用 PyCharm 打开并安装，最后双击打开 py 即可，此时运行的相当于开发版，双击打开后缀为 pyw 的文件为普通版，最大区别就是黑框框。

2. 使用 pyinstall 打包，安装此插件然后打开仓库内的 bat 即可打包。

## 🎈 技术栈 & 原理
  - tkinter：窗体

  - tkinter.messagebox：提示框

  - urllib.request：请求 json

  - json：处理 json

  - jsonpath：处理 json

  - os：操作 cmd

原理很简单，向官方 Api 发起请求（Api是自己抓包抓到的，不知道能用多久），截取返回的数据，然后打开链接，具体代码源里注释写的很清楚。

[^1]: 开发版与普通版区别就是一个有黑框，一个没有黑框

[^2]: 如 jsonpath 和 urllib 等。
