from tele_bot import telegram_chatbot
from os import system
import subprocess


ru=0 # running or not

bot = telegram_chatbot("config.cfg")
# code from https://github.com/SouravJohar/gangsta.git

def make_reply(message):
    reply = None
    global ru
    if message is not None:
        a='0'
    if 'in' in message:  # drowsiness
        system("echo d > cam_mode.txt")
        return "Starting drowsiness detector"
    elif 'out' in message:  # motion
        system("echo m > cam_mode.txt")
        return "Starting motion detector"
    elif 'exit' in message or 'stop' in message:  # exit
        system("echo e > cam_mode.txt")
        #system("echo 0 > cont.txt")
        ru=0
        return "Processes stopped"
    elif "start" in message:
        system("echo d > cam_mode.txt")
        #system("echo 0 > acc.txt")
        #system("echo 1 > cont.txt")
        if ru==0:
            ru=1
            subprocess.Popen(["../Others/venv/bin/python3","drowsiness.py"])
        return "Services started"
    elif "reset" in message:
        system("echo d > cam_mode.txt")
        #system("echo 0 > acc.txt")
        #system("echo 1 > cont.txt")
        ru=1
        return "Resetting"
    else:
        return "Received"#reply


#subprocess.Popen(["python3","main.py"])
# change bashrc run command to run bot.py
# make main.py to stop running on '0' in cont.txt
ru=1
print(make_reply("start"))
system("echo d > cam_mode.txt")
#system("echo 0 > acc.txt ; echo d > cam_mode.txt ; echo 1 > cont.txt")
update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            print(message)
            reply = make_reply(message.lower())
            bot.send_message(reply, from_)

