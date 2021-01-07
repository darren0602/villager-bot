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

        if command == None:
            return

        if command == "$hello" or command == "$HELLO":
            print("Message from {0.author}: {0.content}".format(message))
            await message.channel.send("Hello!")

        if command == "$whois" or command == "$WHOIS":
            print("Message from {0.author}: {0.content}".format(message))

            for arg in args:
                await message.channel.send("{} is {}".format(
                    arg,
                    constants.WHOIS_CHOICES[random.randint(0, len(constants.WHOIS_CHOICES))]
                ))

        if command == "$minecraft" or command == "$MINECRAFT":
            print("Message from {0.author}: {0.content}".format(message))

            # My machine really only has one java process running...
            minecraft_server_filename = "java"

            if utils.check_if_process_running(minecraft_server_filename):
                print("Process {} detected".format(minecraft_server_filename))
                await message.channel.send("Minecraft server is up at {}:25565".format(
                    utils.get_public_ip()
                ))
            else:
                print("No minecraft server process detected!")
                await message.channel.send("Minecraft server is offline :(")

client = MyClient()
client.run(constants.TOKEN)