import datetime
import time
import simpleaudio as sa
from pynput import keyboard
from keyboardlisten import on_press, on_release
import json

def main():
    print("bA Program Started")

    while True:

        currentTime1 = datetime.datetime.now()

        now = currentTime1.strftime('%H:%M')
        day = currentTime1.strftime('%A')
        #print(".")
       
        file = open("alarms.txt", "r")
        diction = file.read()
        file.close()
        
        alarms = json.loads(diction)
        
        for alarm in alarms:
            #print(now + '\n' + day + '\n' + alarm["name"] + "\n" )
            
            if alarm["day"] == "Daily" or alarm["day"] == day:
                if alarm["time"] == now:
                    print('It is now time for', alarm["name"])
                    
                    wave_object = sa.WaveObject.from_wave_file(alarm['sound'])
                    
                    play_object = wave_object.play()
                    print("woow")
                    
                    listener = keyboard.Listener(
                        on_press=lambda event: on_press(event, play_object=play_object),
                        on_release=on_release,
                        play_object=play_object)
                    listener.start()
                    time.sleep(60)
                    #listener.stop()

        time.sleep(20)
                
main()