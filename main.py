# Import Libraries
import discord
import datetime
from discord.ext import commands
import time

# Time Variable
currentTime = datetime.datetime.now()

# Create a new discord client object
client = discord.Client()

# Bot Security Key
botSecurityToken = ("null")

# Welcome Message
print("ModBot Ver 1.3\n\n===System Log===")

# Feature Switches - (0 for off, 1 for on)
profanityFilterSwitch = 0

# ==================
# Security Key Check
# ==================
def secureStart():
   global botSecurityToken
   try:
       securityKeyFile = open("key.bot", "r")      # Open the key file from the same directory as the bot
       botSecurityToken = securityKeyFile.read()   
       try:
           print("Bot Online at: ", currentTime)   # If the login is successful, log it to the console.
           client.run(botSecurityToken)            # Run the discord client and if the token is incorrect, throw an error
       except discord.errors.LoginFailure:        
           print("Error: Incorrect Token.")
           time.sleep(100)
   except FileNotFoundError:                       # If the security key file is missing, give an error.
       print("Error: Missing Security Key File.")
       time.sleep(100)
       
# Words to filter
# TODO: Add a customizable list of filter words (swearList)
                
# ====================
# Chat/Command Section
# ====================
@client.event
async def on_message(message):
    # Hello
    if message.content.find("!hello") != -1:
        print("Command '!hello' Used at: ", currentTime)
        await message.channel.send("Hello there!")
    # Profanity Filter Switch - Adminstrator
    if message.content.find("!togglefilter") != -1:
        # If the filter is already off,
        global profanityFilterSwitch
        if profanityFilterSwitch == 0:                                  
            profanityFilterSwitch += 1
            print("Profanity Filter ON: ", currentTime)
            await message.channel.send("Profanity Filter is now on! :)")
        # If the filter is on,
        else:
            profanityFilterSwitch = 0
            print("Profanity Filter OFF: ", currentTime)
            await message.channel.send("Profanity Filter is now off! :)")
    # ===================
    # Profanity Detection
    # ===================
    if profanityFilterSwitch == 0:
        pass
    else:
        for word in swearList:
            if message.content.count(word) > 0:
                print("Profanity Blocked at: ", currentTime)
                await message.channel.purge(limit=1)
                await message.channel.send("You can't say that here! It's profane!")
                
# ==Start the Bot==
secureStart()