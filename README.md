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
TOKEN=<(str) Your bot token>
MAX_ARGS=<int> Max arguments>
WHOIS_CHOICES=<list(str) Whatever you wanna put>
```

Run the script using `python bot.py`.