import discord
import random
import utils
import constants

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        # Ignore ownself
        if message.author == self.user:
            return

        msg = message.content
        command, args = utils.msg_split(msg)

        if command == "$hello":
            print("Message from {0.author}: {0.content}".format(message))
            await message.channel.send("Hello!")

        if command == "$whois":
            print("Message from {0.author}: {0.content}".format(message))

            for arg in args:
                await message.channel.send("{} is {}".format(
                    arg,
                    constants.WHOIS_CHOICES[random.randint(0, len(constants.WHOIS_CHOICES))]
                ))

client = MyClient()
client.run(constants.TOKEN)