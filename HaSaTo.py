from multiprocessing.connection import wait
import socket
import os
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

methods = open('methods.gif').readlines()
bots = len(methods)

@@ -24,6 +25,8 @@ def special():

def si():
    print('\x1b[38;2;233;233;233mWelcome to HaSaTo DDos ')
    print("")

def special():
    clear()
    si()
    print("             Siiiiiiiii")

@@ -36,6 +37,7 @@ def menu():

def menu():
    clear()
    print("               Ra Menu R lòn")



os.system('cls' if os.name == 'nt' else 'clear')



in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)

def methods():
    clear()
    si()
    print("             Mê Thon Balabalalalalal")
            
def login():
    clear()
    user = "admin"
    passwd = "thanhtrungancut"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Sai rồi nhé ib ChungTrong để cấp lại tool...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to ChungTrong Panel!")
        time.sleep(0.3)
        main()
login()
