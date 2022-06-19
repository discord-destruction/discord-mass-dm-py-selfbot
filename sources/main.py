import asyncio
from datetime import datetime
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='dmdmsb.', intents=discord.Intents.all())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("""\n\n\n\n
        ________  .__                              .___                                                 
        \______ \ |__| ______ ____  ___________  __| _/                                                 
         |    |  \|  |/  ___// ___\/  _ \_  __ \/ __ |                                                  
         |    `   \  |\___ \\  \__(  <_> )  | \/ /_/ |                                                  
        /_______  /__/____  >\___  >____/|__|  \____ |                                                  
                \/        \/     \/                 \/                                                  
           _____                           ________                                                     
          /     \ _____    ______ ______   \______ \   _____                                            
         /  \ /  \\__  \  /  ___//  ___/    |    |  \ /     \                                           
        /    Y    \/ __ \_\___ \ \___ \     |    `   \  Y Y  \                                          
        \____|__  (____  /____  >____  >   /_______  /__|_|  /                                          
                \/     \/     \/     \/            \/      \/                                           
          _________      .__   _____    __________        __                                            
         /   _____/ ____ |  |_/ ____\   \______   \ _____/  |_                                          
         \_____  \_/ __ \|  |\   __\     |    |  _//  _ \   __\                                         
         /        \  ___/|  |_|  |       |    |   (  <_> )  |                                           
        /_______  /\___  >____/__|       |______  /\____/|__|                                           
                \/     \/                       \/                      
        \n\nVersion: 1.0.0                                                                                                               
        \n\n\n\n""")

print("Enter The User Token That You Want To For Doing Some Mass DM: ")
TOKEN = input()



@bot.event
async def on_ready():
    print(f"Logged In As: {bot.user.name}#{bot.user.discriminator}\nWith ID: {bot.user.id}")
    print("Waiting For The Day When I Join A New Server For A Wumpus Mass DM...")

@bot.event
async def on_guild_join(guild: discord.Guild):
    print(f"""Woah! I Just Joined A Server! Do You Want Me To Mass Dm Everybody In It?
    \nServer Information: [Server Creation Date: {guild.created_at}] [Server Name: {guild.name}] [Server ID: {guild.id}]""")
    print("Options: y for yes and n for no (CASE SENSITIVE!)")
    check = input()
    if check == 'y':
        print("What Would You Like The Message To Be?")
        msg = input()
        print(f"Starting Mass Dm Bomb On: {guild.name}/{guild.id}...")
        while True:
            for member in guild.members:
                try:
                    if member is not bot.user:
                        await member.send(msg)
                        print(f"{bcolors.OKGREEN}**** INFO [{datetime.now()}]: --- Sent {member.name}#{member.discriminator} The Message")
                except:
                    print(f"{bcolors.FAIL}**** ERROR [{datetime.now()}]: --- Unable To Send The Message To {member.name}#{member.discriminator} (404 FORBIDDEN [The Users's DM's Are Closed])")
                    pass
    else:
        print("Ok, I Guess We Are Not Doing Any Mass DM Bombs Today! See Ya!")
        await asyncio.sleep(3.6)
        exit()

bot.run(TOKEN)