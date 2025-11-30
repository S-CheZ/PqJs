# <div align="center">PqJs</div>
PyQtWeb引擎逆向工具


经过测试大部分逆向都可以过

直接使用pyqt的web引擎执行js代码并返回sign,省去了补环境的时间,可直接在对应网站进行sign生成.<br/><br/>
分为两个版本：
> 
    命令行版本
    代码版本
## 一,命令行版本
### 1.下载exe or sh
[下载](https://github.com/S-CheZ/PqJs/releases/tag/%E6%B5%8B%E8%AF%95)
### 2.打开命令行执行exe or sh
    
    usage: main.py [-h] [-url URL] input_file
    使用-h可查看命令帮助  url 为可选目标网站   input_file为执行的js代码文件

## 二,代码版本
### 1.拉取代码或复制代码
### 2.调用
        getSign(javascript,url)
        javascript 需要执行的js文本
        url        目标网站（请先不填写url,如若报错或没有结果再填写url）
  
注意：linux中可能需要添加一下环境变量
> export QT_QUICK_BACKEND=software<br/>
> export QMLSCENE_DEVICE=softwarecontext<br/>
> export QT_X11_NO_MITSHM=1<br/>
> export QT_NO_GLUT=1<br/>




<div style="display: flex !important;flex-direction: row;justify-content: space-around;">
  <img src="https://github.com/S-GGbond/PqJs/blob/main/img/wx.jpeg" width="200"  alt="微信群">
  <img src="https://github.com/S-GGbond/PqJs/blob/main/img/qq.jpeg" width="200"  alt="QQ群">
    
</div>
