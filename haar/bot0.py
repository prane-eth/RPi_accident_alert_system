import subprocess
from os import system

cur='0'  # current process
system("echo d > cam_mode.txt")

subprocess.Popen(["python3","main.py"])

def drow():
    system("echo d > cam_mode.txt")

def mot():
    system("echo m > cam_mode.txt")

def read_message():
    msg='a' # use chatbot
    return msg

while True:
    print(1)
    system("sleep 1")
    m=open("./cam_mode.txt").read()  # m=read_message()
    if 'm' in m and 'm' not in cur:
        a='system("echo m > cam_mode.txt")' ; cur='m' ; print(cur)
        subprocess.Popen(["../Others/venv/bin/python3","motion.py"])
    elif 'd' in m and 'd' not in cur:
        a='system("echo d > cam_mode.txt")' ; cur='d' ; print(cur)
        subprocess.Popen(["../Others/venv/bin/python3","drowsiness.py"])
    elif 'e' in m:
        break

# bot should connect to user and write to cam_mode.txt based on input
#    by uing drow() and mot() to write to files. bot should be main file
