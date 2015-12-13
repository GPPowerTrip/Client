# CLI application for Excalibot

# Help
- Provide a description of usage of the botnet
- Help usage: excalibot help COMMAND
- General usage: excalibot COMMAND HOST PORT [PARAMETERS]

## COMMAND
- help    Print usage
- list    List available bots
- attack  Schedule new attacks
- install Install new plugin
- status  Check task completion status
- clear   Clear task from control center


# List
- List available bots
- Usage: excalibot list HOST PORT KEY

## KEY
- id          Sort list by botid
- ipAddress   Sort list by IP address
- lastSeen    Sort list by seconds since last report')
- os          Sort list by Operative System
- countryCode Sort list by Country
- zip         Sort list by zip code


# Attack
- Schedule new attacks
- Usage: excalibot attack HOST PORT ATTACK [KEY:VALUE]

## ATTACK
- Name of installed plugins

## KEY:VALUE
- Parameters to the attack, order does not matter, use a key:value format (ex: time:5)
- TODO get plugins from server


# Install
- Install new plugin
- Usage: excalibot install HOST PORT URL

## URL
- Url to the plugin resource


# Status
- Check task completion status
- Usage: excalibot status HOST PORT ID (-b)

## ID
- Id of the task to get status

## -b
- Optional, use -b to block until task is completed


# Clear
- Clear task from control center
- Usage: excalibot clear HOST PORT ID

## ID
- Id of the task to deleted
