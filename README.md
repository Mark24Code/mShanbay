# mShanbay

#####基于Django的实验项目

####目标:

适用于手机端的，一个简单的背单词 web app

* 展示 单词，释义，同义词
* 可以设置每天背多少单词
* 可以根据四级,六级，托福和雅思来设置自己的单词范围
* 每个 用户可以添加笔记，也可以查看其它用户的共享笔记
* 收藏单词
* 单词进度
* 校验 x
* 手机适配 (目前试验了 红米Note2) x
* 动态加载 x
* 专业词库 x
* 美腻的UI x
* 用户信息(头像之类的) x
* 使用数据展示 x
....

---
####开发环境

>环境依赖

>* Python==3.5
* Django==1.8
* PyMySQL==0.7.2

>数据库

>* MySQL== 5.5


---

####配置与运行


1. 安装Python3,见官网

2. 项目一级目录下，执行安装依赖 `pip install -r requirement.txt`

3. 根据 `mshanbay/setting.py` 文件配置 MySQL

4. 执行一级目录下 `rebuild` 脚本

5. 执行一级目录下 `runserver` 脚本

6. 假设电脑与手机在同一局域网下，电脑 IP为 `192.168.1.100`，手机请访问 `http://192.168.1.100:8000/`

---

####效果展示

* 登录页

![登录页](http://ww4.sinaimg.cn/mw690/44894cbbgw1f44mxpk53qj20u01hc76d.jpg)

* 配置界面

![配置](http://ww4.sinaimg.cn/mw690/44894cbbgw1f44nqhqi07j20u01hcq6s.jpg)

![选择](http://ww2.sinaimg.cn/mw690/44894cbbgw1f44nqj3nhwj20u01hc41l.jpg)

* 背单词界面,单词进度,自定义笔记，用户共享笔记

![单词界面](http://ww3.sinaimg.cn/mw690/44894cbbgw1f44mxr8c2xj20u01hcwib.jpg)

* 新建笔记

![单词界面](http://ww3.sinaimg.cn/mw690/44894cbbgw1f44mxr0tr8j20u01hc799.jpg)

* 完成任务

![完成任务](http://ww3.sinaimg.cn/mw690/44894cbbgw1f44nqhk6e6j20u01hc0vq.jpg)








