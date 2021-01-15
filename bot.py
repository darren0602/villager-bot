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

        # Only log messages that start
        # with the '$' prefix.
        if msg.startswith("$"):
            print("Message from {0.author}: {0.content}".format(message))

        # Delete sender commands after 3 seconds delay
        # Also delete command with prefix - (groovy)
        # to prevent clutter.
        if msg.startswith("-") or msg.startswith("$"):
            await message.delete(delay=3)

        """
        $help: Shows all available commands.
        """
        if utils.is_valid_command(command, "help"):
            await message.channel.send(defaults.HELP_MSG)
            return

        """
        $hello: Says hello back to you in case you're lonely.
        """
        if utils.is_valid_command(command, "hello"):
            await message.channel.send("Hello!")
            return

        """
        $whois <user1> <user2> <user3>: Tells you what kind of person each user is.
        """
        if utils.is_valid_command(command, "whois"):
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

        """
        $location: Tells you the server location. Aliases: $region, $where.
        """
        if utils.is_valid_command(command, "location", alternative_commands=["region", "where"]):
            guild_id = message.guild.id
            region = self.get_guild(guild_id).region

            await message.channel.send("We are in {}".format(
                region
            ))

# Run test
test_results = tests.setup_test()
if test_results == False:
    print("Exiting...")
    exit(-1)

client = MyClient()
client.run(constants.TOKEN)