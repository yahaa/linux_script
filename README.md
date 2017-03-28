# linux_script
### 关于
该脚本为linux 系统一键配置java环境脚本

### 使用
* 把项目克隆到本地
* cd path_script
* sudo su
* python paths.py

### 说明
* 该脚本需要 root 权限运行
* 脚本运行结束电脑会自动重启
* 重启后 java 环境已经配置好了
* 使用前先看看代码，考虑后再运行
* 如果由于网络问题无法下载，会导致错误的配置，解决错误只需要 把 /opt/jdk****删掉，把 /etc/profile里面的 # JAVA PATH 下面有关java的配置删掉即可
