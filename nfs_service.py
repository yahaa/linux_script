import os
cmd = ['apt-get update', 'apt-get install nfs-kernel-server nfs-common',
       'mkdir /home/public', 'chmod -R 777 /home/public',
       'echo "/home/public  *(rw,sync,no_root_squash)" >>/etc/exports', 'service rpcbind start', 'service nfs-kernel-server start']


def install():
    for item in cmd:
        os.system(item)


if __name__ == '__main__':
    install()
