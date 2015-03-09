# -*- coding:utf-8 -*-
# PROJECT_NAME : saltstack-utils
# FILE_NAME    : 
# AUTHOR       : younger shen

import os

PATH = os.getcwd()
MINION_PATH = PATH + '/minion/minion'


def minion_config_install():
    os.popen('cp ' + MINION_PATH + ' /etc/salt/minion')
