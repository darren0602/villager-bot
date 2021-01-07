# VillagerBot

![villager.png](villager.png)

## Setting up

Set up a virtualenv and install pip packages.

```bash
python3 -m venv villager-bot
source villager-bot/bin/activate
pip install -r requirements.txt
```

Create a `constants.py` file and add

```
TOKEN=<(str, required) Your bot token>
MAX_ARGS=<(int) Max arguments>
WHOIS_CHOICES=<list(str) Whatever you wanna put>
```

Run the script using `python bot.py`.

## Commands
Available commands:
```
$help: Shows all available commands.
$hello: Says hello back to you in case you're lonely.
$whois <user1> <user2> <user3>: Tells you what kind of person each user is.
```
