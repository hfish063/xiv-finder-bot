# xiv-finder-bot

## Description
**xiv-finder-bot** is a personal project of mine.  It provides the ability for discord users to perform various requests from the *XIVAPI* through a command interface.  Additionally, you may obtain info regarding the latest game news through the *Lodestone Api*.

## Guide
### Category types
**Accepts:** Achievement, Title, Action, CraftAction, Trait, PvPAction, PvPTrait, Status, BNpcName, ENpcResident, Companion, Mount, Leve, Emote, InstanceContent, Item, Recipe, Fate, Quest, ContentFinderCondition, Balloon, BuddyEquip, Orchestrion, PlaceName, Weather, World, Map, lore_finder

### General commands
1. `!search [categoryname] [string]`
    - Where **string** is the name of object to search for
    - Performs wildcard search (result list is limited to **5 items**)
2. `!match [categoryName] [string]`
    - Performs **match** search, (only exact matches to string argument are returned)
3. `!topics optional:[result_limit]`
    - Sends list of this month's news topics
    - Length of result list depends on optional command argument (default is 10)
4. `!maintenance`
    - Sends list of this month's maintenance (server downtime) events
6. `!status`
    - Checks current game and lodestone servers for (**ongoing**) maintenance

## Additional Info
### Install guide
**NOTE:** xiv-finder-bot is not *currently* being hosted for public use, in order to utilize the bot you must host it on your local machine

- `pip3 install -r requirements.txt` 
- `pip install -r requirements.txt` *Windows*

<a href="url"><img src="https://github.com/hfish063/xiv-finder-bot/assets/123512041/92332601-38a4-4d1b-b948-fa5ec2c78723" height="240" width="240" ></a>
