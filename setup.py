# -*- coding:utf-8 -*-
# PROJECT_NAME : saltstack-utils
# FILE_NAME    : 
# AUTHOR       : younger shen

import sys
import os
sys.path.append(os.getcwd())

import argparse
from master.setup import master_config_install
from minion.setup import minion_config_install
parser = argparse.ArgumentParser(description='acttao saltstack utils for development configuration')
parser.add_argument('cmd', help='should always be install', choices=['install'])
parser.add_argument('type', help='should be master or minion', choices=['master', 'minion'])

args = parser.parse_args()

if args.cmd and args.type == 'master':
    master_config_install()

if args.cmd and args.type == 'minion':
    minion_config_install()
