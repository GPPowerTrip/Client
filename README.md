```
help help
    ('Usage: excalibot help COMMAND')
    ('General application usage: excalibot COMMAND HOST PORT PARAMETERS')
    ('COMMAND:')
    ('  help\t\t this information')
    ('  bot_list\t\tList available bots')
    ('  task_submit\tSchedule new attacks')
    ('  task_list\tList running tasks')
    ('  task_status\tCheck task completion status')
    ('  task_output\t completed task output')
    ('  task_clear\t\tClear task from control center')
    ('  plugin_install\t\tInstall new plugin')
    ('  plugin_list\t\tList installed plugins')
    ('  plugin_clear\t\tClear installed plugin')
    ('  plugin_help\t\tGet help for installed plugin')

help bot_list
    ('List available bots')
    ('Usage: excalibot bot_list HOST PORT key:KEY since:SINCE')
    ('KEY: (optional)')
    ('  id\t\tSort list by botid')
    ('  ipAddress\tSort list by IP address')
    ('  lastSeen\tSort list by seconds since last report')
    ('  os\t\tSort list by Operative System')
    ('  countryCode\tSort list by Country')
    ('  zip\t\tSort list by zip code')
    ('SINCE: (optional)')
    ('  Show only bots alive in the last SINCE seconds')

help task_submit
    ('Schedule new tasks')
    ('Usage: excalibot task_submit HOST PORT ATTACK KEY:VALUE')
    ('ATTACK:')
    ('  installed plugin name')
    ('KEY:VALUE: (optional)')
    ('  list of parameters to the attack, in a key:value format')

help task_list
    (' list of ongoing tasks')
    ('Usage: excalibot task_list HOST PORT')

help task_status
    ('Check task completion status')
    ('Usage: excalibot task_status HOST PORT ID block')
    ('ID:')
    ('  id of the task to get status')
    ('block: (optional)')
    ('  block until task is completed')

help task_output
    (' task output')
    ('Usage: excalibot task_output HOST PORT ID')
    ('ID:')
    ('  id of the task to get output')

help task_clear
    ('Clear task from control center')
    ('Usage: excalibot task_clear HOST PORT ID')
    ('ID:')
    ('  id of the task to deleted')

help plugin_install
    ('Install new plugin')
    ('Usage: excalibot plugin_install HOST PORT name:NAME url:URL')
    ('NAME:')
    ('  name of the plugin ')
    ('URL:')
    ('  url to the plugin resource')

help plugin_list
    (' list of available plugins')
    ('Usage: excalibot plugin_list HOST PORT')

help plugin_clear
    ('Clear plugin from control center')
    ('Usage: excalibot task_clear HOST PORT NAME')
    ('NAME:')
    ('  name of the plugin to deleted')

help plugin_help
    ('Get help for installed plugin')
    ('Usage: excalibot plugin_help HOST PORT NAME')
    ('NAME:')
    ('  name of the plugin to get help')
```
