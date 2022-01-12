## mcserver-discord

simple discord.py program that will look-up any java edition minecraft server using Dinnerbone's official mcstatus library. the info is then sent into a nicely formatted embed in the channel and message of your choosing.

### REQUIRED LIBRARIES

`py -m pip install discord`
`py -m pip install mcstatus`
`py -m pip install asyncio`

## init

before you can run `minecraft.py`, edit your config (leaving out `message_id` for now) then run `mc_send.py`. this will send a placeholder message in the designated channel found in config. copy the message id of the placeholder message and place it in the `message_id` config.

## start

you can now just run `minecraft.py` on-startup, on a 24/7 server or whatever you want. just ensure that `config.json` is stored in the same directory and that the code doesn't randomly explode cus this was originally only created for my own use but here we are. leave any bug reports in the issues tab.

## config

all config for the bot is held within the `config.json` file, including the bot's token which is required to run the bot for your server (obviously can't run the bot as the config for the server ip etc. is per-person)

| value | description |
|-------|-------------|
| token | place your bot's token here |
| server_ip | your mc server's ip (include port eg. 127.0.0.1:25565) |
| server_formal_ip | if you can connect to your server with a user-friendly domain, put it here (or just put the ip again) |
| server_name | the name used for your embed header |
| player_limit | what to display for your player count (eg. 2/50) |
| channel | the discord #channel the bot's message is contained in |
| message_id | the message id of the bot's message |
