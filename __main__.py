#!/usr/bin/env python

from classes.options import Options
import sys

# Option variables
op = sys.argv[1]
param = sys.argv[2:]
ops = ['help', 'list', 'attack', 'install', 'status', 'clear']

# Sanitation of parameters
if len(sys.argv) < 2 or op not in ops:
    print('>>Invalid command.\n>>Use help for a list of commands.')
    sys.exit()

# Execution of operations
result = getattr(Options, op)(param)
