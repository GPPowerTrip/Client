#!/usr/bin/env python

from classes.options_test import Options
import sys

ops = ['help', 'bot_list', 'task_submit', 'plugin_install', 'task_status', 'task_clear', 'task_output', 'task_list',
       'plugin_list', 'plugin_clear', 'plugin_help']
if len(sys.argv) < 2 or sys.argv[1] not in ops:
    print('Invalid command.\nUse help for a list of commands.')
else:
    getattr(Options, sys.argv[1])(sys.argv[2:])

