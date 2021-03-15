# AutoClicker made by noni @ 2019

# Choose a button to toggle autoclicking
# Choose a button to stop the program

# Clicking stops once you moved the mouse from the position you initiated the
# clicking action in order to protect from potential mishaps when inadvertently
# moving it

# FIRST WORKING SCRIPT

import time
import threading
import sys

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


_delay = 0.01

if len(sys.argv) > 1:
    if type(sys.argv[1]) is float:
        _delay = float(sys.argv[1])
    else:
        _delay = 0.001
else:
    _delay = 0.001


_start_stop_key = KeyCode(char='e')
_exit_key = KeyCode(char='a')
_button = Button.left

_pos_at_start = (0, 0)

mouse = Controller()


class ClickMouse(threading.Thread):

    def __init__(self, delay, button, pos_at_start):
        super().__init__()
        self.delay = delay
        self.button = button
        self.pos_at_start = pos_at_start
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
        self.pos_at_start = mouse.position
        print(self.pos_at_start)

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                pos = mouse.position

                if pos == self.pos_at_start:
                    pos = mouse.position
                    mouse.click(self.button)
                    time.sleep(self.delay)
                else:
                    self.stop_clicking()
                    break


click_thread = ClickMouse(_delay, _button, _pos_at_start)

click_thread.start()


def on_press(key):
    global _pos_at_start
    if key == _start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            _pos_at_start = mouse.position
            click_thread.start_clicking()



    elif key == _exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
