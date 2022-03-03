#Created by Aurora Knish
#Version 1.0.1

import numpy as np
from datetime import datetime, timedelta
import pytz
import tweepy
import telepot
import time as tmtime
global TIME5MINUTES
from threading import Thread
from time import sleep
from pathlib import Path
import yaml
import os
import sounddevice as sd
THREADRUNONCE = False

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def get_file_contents(filename): #Get the contents of the API key file
    API_FILE = filename
    with open(API_FILE, 'r') as config_file:
        config = yaml.load(config_file)
    return config

def timer():
    global THREADRUNONCE
    global TIME5MINUTES
    global IMAGEFILE
    global CHANNELID
    global TOWNNAME
    sleep_duration = 4 #The time the sound should run until it considers it a siren
    Ukraine_Time = datetime.now(tz).strftime('%H:%M:%S')
    Ukraine_Date = datetime.now(tz).strftime('%d/%m/%Y')
    while sleep_duration > 0:
        if(STOP_THREAD == True):
            print("Thread stopped at " + str(sleep_duration) + ' - ' + str(VOLUME_NORM))
            break
        else:
            print(f"Sound has {sleep_duration} seconds left until alert is triggered ")
            sleep(1)
            sleep_duration -= 1
    if(sleep_duration == 0 ):
        print('(' + str(VOLUME_NORM) + ') Time: ' + str(Ukraine_Time) + '  -  SIREN')
        if(datetime.strptime(Ukraine_Time,'%H:%M:%S') > datetime.strptime(TIME5MINUTES,'%H:%M:%S')):
            text = 'Ukraine Siren Alert [' + str(Ukraine_Date) + ']\n\n' + Ukraine_Time + '\n' + TOWNNAME + '\n\nMessage was generated using live stream data. If wrong please contact us.\n#Ukraine'
            
            api.update_with_media(IMAGEFILE,status=text)
            bot3 = telepot.Bot(apikeys['telepot']['api_key'])
            bot3.sendPhoto(CHANNELID, photo = open(IMAGEFILE, 'rb'),caption=f'{text}',parse_mode="Markdown")
            TIME5MINUTES = (datetime.strptime(Ukraine_Time,'%H:%M:%S') + timedelta(minutes=15)).strftime('%H:%M:%S')
            print('Posting blocked until ' + TIME5MINUTES)
    
    THREADRUNONCE = False


def main():
    try:
        with sd.Stream(callback=print_sound):
            sd.sleep(-1)
    except KeyboardInterrupt:
        print("Stopped")
def print_sound(indata, outdata, frames, time, status):
    global VOLUME_NORM
    global STOP_THREAD
    global THREADRUNONCE
    try:
        VOLUME_NORM = np.linalg.norm(indata)*10
        print(VOLUME_NORM)
        if(int(VOLUME_NORM) > 35): #volume level to trigger the script
            STOP_THREAD = False
            
            if(THREADRUNONCE is False):
                THREADRUNONCE = True
                timer_thread = Thread(target=timer)
                
                timer_thread.start()
        else:
            STOP_THREAD = True
    except:
        quit

# Authenticate to Twitter
apikeys = get_file_contents('auth.yaml')
auth = tweepy.OAuthHandler(apikeys['twitter']['consumer_key'], apikeys['twitter']['consumer_secret'])
auth.set_access_token(apikeys['twitter']['access_token'], apikeys['twitter']['access_token_secret'])
TOWNNAME = 'Kyiv' #Set the towns name
import os
print(os.name)
if os.name == 'nt':
    IMAGEFILE = dname + '\\images\\' + TOWNNAME + '.png' #Attempt to load the image file (Windows)
else:
    IMAGEFILE = dname + '/images/' + TOWNNAME + '.png' #Attempt to load the image file (Linux)
CHANNELID = -1001511264252 #Telegram channel ID

api = tweepy.API(auth) # Create API object
tz = pytz.timezone('Europe/Kiev') # Set a timezone for the time of the alerts
TIME5MINUTES = datetime.now(tz).strftime('%H:%M:%S')
if Path(IMAGEFILE).is_file():
    print ("Image file exists!")
else:
    print ("Image file does not exist. Closing program.")
    quit()
if __name__ == "__main__":
    main()
