# saltstack 作业

* 概述
* 功能及使用方法
* 难点
* 总结

---------------------------

__概述__

主要功能是要通过saltstack去管理开发人员的开发环境，但是每个人都有自己的安装软件的习惯,我习惯自己编译vim, python和php，所以这里只做了３个配置,分别是 __python环境__, __pycharm安装__ 和 __mysql__, 非常简单的配置文件，只有十几行,结合一个python脚本去复制文件到各个目录，非常简单.

----------------------------

__功能和使用方法__

使用方法:

    1. 克隆配置文件到本地
    2. 在master和minion分别安装salt-master和satl-minion(pip的安装方式不不会安装zeromq,可以采用apt-get安装或者是python setup.py install的方式安装).
    3. 在配置文件的根目录执行 python setup.py install master 和 python setup.py install minion, 复制配置文件和相应的SLS文件到相关目录
    4. 由于pycharm是一个tarball，所以需要分别设置windows和linux下不同的软件包, linux下的名字叫做 pycharm.tar.gz, windows下的名字叫做　pycharm.rar, 放在 /etc/salt/base目录下即可，软件包会被分别复制到　/usr/local/tools/pychar.tar.gz和 D:/dev/pycharm.rar.
    5. windows的repo只有４个软件，分别是　python 2.7 x86 python 2.7 x64 pycharm和mysql5.6社区版本.
    6. 配置好以后，分别执行　sudo salt-master -d 和 sudo salt-minion -l debug & 来开始调试模式看是否执行成功
    7. 执行sudo salt state.highstate 来同步文件，没有报错的话就执行成功了.
    8. 执行 salt -N python_dev_new test.ping 和 salt -N web_dev_new test.ping 来分别发送命令给２个组，
    9. system_status　这个 grain　用来区别是否是新系统，为了不同时向所有的minion发送同步命令,minion可以在更新文件之后修改掉这个 grain的值.


__难点__

主要的难点是对于linux操作系统的理解，还有就是英文水平,英文水平的好坏对是否能快速掌握该软件起了重要的作用,而且其中的很多高级技巧都没有用到，比如自定义grain,自定义model和自定义可执行model等，　而且该软件的最新版是有bug的，可以参见之前的文档.

-------------------------

__总结__

学习到了好多东西，包括stalkstack的使用方法和配制方法，很多英文单词和linux相关的东西，了解到了zeromq和其他mq的不同，不到位的地方是，由于第一次接触运维相关的东西，所以很多命令很生疏，产出的东西也不太好用(主要是不清楚应用场景)，而且想快速开始开发的工作，所以，请让我写代码吧!


 