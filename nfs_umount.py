import os
cmd = ['umount 115.29.146.79:/home/public',
       'service rpcbind stop', 'service nfs-kernel-server stop']


def shudown():
    for item in cmd:
        os.system(item)


if __name__ == '__main__':
    shudown()
