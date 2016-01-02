#!/usr/bin/env python

from classes.options_test import Options
import sys

ops = ['help', 'list', 'attack', 'install', 'status', 'clear', 'output']
if len(sys.argv) < 2 or sys.argv[1] not in ops:
    print('Invalid command.\nUse help for a list of commands.')
else:
    getattr(Options, sys.argv[1])(sys.argv[2:])

