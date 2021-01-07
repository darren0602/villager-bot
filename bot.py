import discord
import random
import utils
import constants
import defaults
import tests

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        # Ignore ownself
        if message.author == self.user:
            return

        msg = message.content
        command, args = utils.msg_split(msg)

        # Ignore messages that aren't
        # command calls.
        if command == None:
            return

        if command == "$help" or command == "$HELP":
            print("Message from {0.author}: {0.content}".format(message))
            await message.channel.send(defaults.HELP_MSG)
            return

        if command == "$hello" or command == "$HELLO":
            print("Message from {0.author}: {0.content}".format(message))
            await message.channel.send("Hello!")
            return

        if command == "$whois" or command == "$WHOIS":
            print("Message from {0.author}: {0.content}".format(message))

            # Use default value if constants
            # not properly setup by user
            try:
                WHOIS_CHOICES = constants.WHOIS_CHOICES
            except AttributeError:
                WHOIS_CHOICES = defaults.WHOIS_CHOICES

            for arg in args:
                await message.channel.send("{} is {}".format(
                    arg,
                    WHOIS_CHOICES[random.randint(0, len(WHOIS_CHOICES) - 1)]
                ))
            return

# Run test
test_results = tests.setup_test()
if test_results == False:
    print("Exiting...")
    exit(-1)

client = MyClient()
client.run(constants.TOKEN)