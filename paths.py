import os
from os.path import getsize


def buildJavaPath():
    path = '# JDK PATH\n\
    export JAVA_HOME=/opt/jdk1.8.0_121\n\
    export JRE_HOME=/opt/jdk1.8.0_121/jre\n\
    export CLASSPATH=.:\$JAVA_HOME/lib:\$JRE_HOME/lib:\$CLASSPATH\n\
    export PATH=\$JAVA_HOME/bin:\$JRE_HOME/bin:\$PATH'

    cmd = ['wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz -O jdk1.8.tar.gz', \
    'tar -xzvf jdk1.8.tar.gz', 'cp -r jdk1.8.0_121 /opt',
           'echo "' + path + '" ' + '>> /etc/profile', 'init 6']
    net = False
    nex = False
    res = os.popen('ping www.baidu.com -c 1 -w 5').readlines()
    for item in res:
        s = str(item)
        if s.find('bytes from'):
            net = True
    if net == False:
        print 'Unable to link network !'
        return

    s = str(os.environ)
    if s.find('jdk') < 0:
        nex = True
    if nex ==False :
        print 'JDK already exists !'
        return 

    if net and nex:
        os.system(cmd[0])

    jdksize = getsize('jdk1.8.tar.gz')
    if jdksize <180000000:
        print 'Download error !'
        return
        
    for item in cmd[1:-1]:
        os.system(item)


if __name__ == '__main__':
    buildJavaPath()
