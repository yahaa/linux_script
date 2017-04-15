import os
cmd = ['apt-get update', 'apt-get install rcpbind',
       'apt-get install nfs-client', 'service rpcbind start',
       'mkdir /home/nfsshare', 'mount -t nfs 115.29.146.79:/home/public /home/nfsshare',
       'chmod -R 777 /home/nfsshare']


def install():
    for item in cmd:
        os.system(item)


if __name__ == '__main__':
    install()
