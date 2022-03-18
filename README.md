# Cloud-Music-Tool
Pyrhon制作的网易云音乐歌曲获取工具

## 正常使用

点此下载 Windows 版本：[https://raw.fastgit.org/Offline2008/Cloud-Music-Tool/main/dist/main.exe](https://raw.fastgit.org/Offline2008/Cloud-Music-Tool/main/dist/main.exe)

下载完成双击打开，如图操作：

![](https://gitee.com/offline2008/img/raw/master/Snipaste_2022-03-18_13-20-39.jpg)

## 如何使用
### 运行
Clone整个仓库，需要安装部分组件，可以使用 PyCharm 打开安装，最后双击打开 py 即可，如果需要隐藏命令符，把 py 后缀改为 pyw 即可。
### 打包
使用 pyinstall 打包，安装此插件打开仓库内的 bat 即可打包。

## 原理
原理很简单，向官方 Api 发起请求（Api是自己抓包抓到的，不知道能用多久），截取返回的数据，然后打开链接。
