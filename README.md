# TelegramBots

In this repository you will find all the Telegram bots I've programed.
Some of them have their own repos because of their complexity, but they are still include in this one.

It's designed so that you can run any of the bots from this one repo. Just type your TOKEN in an _.env_ file, chouse a bot and run it.

## Set up

Make a copy of _.env.example_ and rename it to _.env_

```bash
cp .env.example .env
```

Paste your Telegram bot TOKEN in the new _.env_ file.

> If you don't know how to get a TOKEN, [I have a video on the topic](https://youtu.be/h1QGky22b-k)

## Run

Now just pick any of the bot files and run them with Python3.

```bash
python3 Base.py
```

Since it takes the token form the _.env_ file you don't need to change any of the files.

Now try talking with your bot.

# Bot List

| Bot Name | Function | File Name |
| - | - | - |
| Base | It is the base template for developing better | Base.py |
| DonQuijoteBot | Takes user mesagges and reponds with how many times it apears in _[Don Quijote](https://en.wikipedia.org/wiki/Don_Quixote)_ | DonQuijoteBot.py |
