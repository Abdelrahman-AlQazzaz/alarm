#!/usr/env/bin python3
from pynput import keyboard

SHORTCUTS = [{keyboard.Key.cmd, keyboard.KeyCode(char='c')}]
pressed = set()

def on_press(key, play_object):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        
        if str(key.vk) == '269025073':
            play_object.stop()
            print("stopped")
            return False
            
        if any([key in combo for combo in SHORTCUTS]):
            pressed.add(key)
            if any(all(k in pressed for k in combo) for combo in SHORTCUTS):
                print('pressed {}'.format(SHORTCUTS))
        
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    
    if any([key in combo for combo in SHORTCUTS]):
        pressed.remove(key)
        
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
'''with keyboard.Listener(
        on_press=lambda event: on_press(event, play_object='asdsada'),
        on_release=on_release) as listener:
    listener.join()'''