## mcserver-discord

simple discord.py program that will look-up any java edition minecraft server using Dinnerbone's official mcstatus library. the info is then sent into a nicely formatted embed in the channel and message of your choosing.

### REQUIRED LIBRARIES

```
py -m pip install discord
py -m pip install mcstatus
py -m pip install asyncio
py -m pip install colorama
```

## init

1. open up `config.json` and enter in the `channel` entry.
2. then run **`mc_send.py`**  to send a placeholder message.
3. copy the placeholder's message id into the `message_id` entry

## start

you can now mess with the bot's config (reference below) and start up `minecraft.py` on a 24/7 server or whatever you want. leave issues on this github page and i'll try and fix them.

## config

all config for the bot is held within the `config.json` file, including the bot's token which is required to run the bot for your server.

| value | description |
|-------|-------------|
| token | place your bot's token here |
| server_ip | server's full ip (eg. 127.0.0.1:25565 **include port**) |
| server_formal_ip | server's user-friendly domain (eg. `mc.hypixel.net`) |
| server_name | server's embed header name |
| player_limit | max server player count |
| ignore_no_query | read [here](enable_query.md) for more info (`true`/`false`) |
| channel | the discord #channel the bot's message is contained in |
| message_id | the message id of the bot's message |
