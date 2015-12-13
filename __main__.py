#!/usr/bin/env python

from classes.options import Options
import sys

ops = ['help', 'list', 'attack', 'install', 'status', 'clear']
if len(sys.argv) < 2 or sys.argv[1] not in ops:
    print('>>Invalid command.\n>>Use help for a list of commands.')
else:
    getattr(Options, sys.argv[1])(sys.argv[2:])

