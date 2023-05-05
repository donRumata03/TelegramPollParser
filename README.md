# TelegramPollParser
Parses all polls from a telegram chat: stores all info in separate jsons

It's a part of the _poll-analyzing project_: poll results from [this](https://t.me/Oprosivishka) TG chat.

It uses `telethon` python library which communicates with tg server via the API for client applications.

## How to contribute your _computation power_

The recipe is simple: 

1. git pull/clone
2. create your local `config.py` file (it's .gitignore'd) with these variable definitions:
 ```python
 api_id, api_hash, # follow instructions from here to get this values: https://core.telegram.org/api/obtaining_api_id
 chat_id = -1001647040185, phone
 ```
3. Run the application until you are thrown from your account (that's typically around 100 messages)
4. git commmit & git push
