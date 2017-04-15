# linux_script
### 关于
该脚本为linux 系统一键配置java环境脚本

### java_path.py 使用
* 把项目克隆到本地
* cd path_script
* sudo su
* python java_path.py

### nfs文件系统配置脚本使用说明(服务器端 需要 root 权限)
* git clone git@github.com:yahaa/path_script.git
* cd path_script
* sudo su
* python nfs_service.py
* 停止服务 python nfs_umount.py

### nfs 客户端配置(需要 root 权限)
* git clone git@github.com:yahaa/path_script.git
* cd path_script
* sudo su
* python nfs_client.py
* 卸载 nfs python nfs_umount.py

### java_path 说明
* 该脚本需要 root 权限运行
* 脚本运行结束电脑会自动重启
* 重启后 java 环境已经配置好了
* 使用前先看看代码，考虑后再运行
* 如果由于网络问题无法下载，会导致错误的配置，解决错误只需要 把 /opt/jdk****删掉，把 /etc/profile里面的 # JAVA PATH 下面有关java的配置删掉即可

### 声明
* 该项目脚本是本人常用的一些脚本，运行需要root权限，若因使用本项目的脚本导致个人数据丢失，本人概不负责。
