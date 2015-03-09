#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# PROJECT_NAME : saltstack-utils
# FILE_NAME    : 
# AUTHOR       : younger shen

import os
PATH = os.getcwd()
MASTER_PATH = PATH + '/master/master'
BASE_PATH = PATH + '/master/base'
PILLAR_PATH = PATH + '/master/pillar'
PYTHON_DEV_PATH = PATH + '/master/python_dev'
WIN_REPO_PATH = PATH + '/master/win'


def master_config_install():
    os.popen('cp -r ' + MASTER_PATH + ' /etc/salt/master').readlines()
    os.popen('cp -r ' + BASE_PATH + ' /srv/salt/')
    os.popen('cp -r ' + PILLAR_PATH + ' /srv/')
    os.popen('cp -r ' + PYTHON_DEV_PATH + ' /srv/salt/')
    os.popen('cp -r ' + WIN_REPO_PATH + ' /srv/salt/')

if __name__ == '__main__':
    master_config_install()

