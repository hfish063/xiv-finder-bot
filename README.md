# xiv-finder-bot

## Description
**xiv-finder-bot** is a personal project of mine.  It provides the ability for discord users to perform various requests from the *XIVAPI* through a command interface

## Guide
### Category types
**Accepts:** Achievement, Title, Action, CraftAction, Trait, PvPAction, PvPTrait, Status, BNpcName, ENpcResident, Companion, Mount, Leve, Emote, InstanceContent, Item, Recipe, Fate, Quest, ContentFinderCondition, Balloon, BuddyEquip, Orchestrion, PlaceName, Weather, World, Map, lore_finder

### General commands
1. `!search [categoryname] [string]`
    - Where **string** is the name of object to search for
    - Performs wildcard search (result list is limited to **5 items**)
2. `!match [categoryName] [string]`
    - Performs **match** search, (only exact matches to string argument are returned)

## Additional Info
### Install guide
**NOTE:** xiv-finder-bot is available for public use, no downloads necessary! If you wish to host your own bot, you will need the required dependencies

- ```pip3 install discord```
- ```pip3 install requests```
- ```pip3 install os```
- ```pip3 install python-dotenv```
