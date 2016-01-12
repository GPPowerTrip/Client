#!/usr/bin/env python


def help():
    print('Usage: excalibot help COMMAND')
    print('General application usage: excalibot HOST PORT COMMAND PARAMETERS')
    print('COMMAND:')
    print('  help            # Print this information')
    print('  knight_ls       # List available bots')
    print('  task_run        # Schedule new attacks')
    print('  task_ls         # List running tasks')
    print('  task_check      # Check task completion status')
    print('  task_output     # Print completed task output')
    print('  task_rm         # Clear task from control center')
    print('  plugin_install  # Install new plugin')
    print('  plugin_ls       # List installed plugins')
    print('  plugin_rm       # Clear installed plugin')
    print('  plugin_help     # Get help for installed plugin')


def knight_ls():
    print('List available bots')
    print('Usage: excalibot HOST PORT knight_ls SINCE')
    print('SINCE: (optional)')
    print('  Show only bots alive in the last SINCE seconds')


def task_run():
    print('Schedule new tasks')
    print('Usage: excalibot HOST PORT task_run ATTACK KEY:VALUE')
    print('ATTACK:')
    print('  installed plugin name')
    print('KEY:VALUE: (optional)')
    print('  list of parameters to the attack, in a key:value format')


def task_ls():
    print('Print list of ongoing tasks')
    print('Usage: excalibot HOST PORT task_ls')


def task_check():
    print('Check task completion status')
    print('Usage: excalibot HOST PORT task_check ID block')
    print('ID:')
    print('  id of the task to get status')
    print('block: (optional)')
    print('  block until task is completed')


def task_output():
    print('Print task output')
    print('Usage: excalibot HOST PORT task_output ID')
    print('ID:')
    print('  id of the task to get output')


def task_rm():
    print('Clear task from control center')
    print('Usage: excalibot HOST PORT task_rm ID')
    print('ID:')
    print('  id of the task to deleted')


def plugin_install():
    print('Install new plugin')
    print('Usage: excalibot HOST PORT plugin_install URL')
    print('URL:')
    print('  url to the plugin resource')


def plugin_ls():
    print('Print list of available plugins')
    print('Usage: excalibot HOST PORT plugin_ls')


def plugin_rm():
    print('Clear plugin from control center')
    print('Usage: excalibot HOST PORT task_rm NAME')
    print('NAME:')
    print('  name of the plugin to deleted')


def plugin_help():
    print('Get help for installed plugin')
    print('Usage: excalibot HOST PORT plugin_help NAME')
    print('NAME:')
    print('  name of the plugin to get help')
