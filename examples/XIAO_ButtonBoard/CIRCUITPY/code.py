#https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/CircuitPython_Essentials/CircuitPython_HID_Keyboard/code.py
#License: MIT
#Board: XIAO RP2040

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keycode_jp import KeycodeJP
from keyboard_layout_jp import KeyboardLayoutJP

# A simple neat keyboard demo in CircuitPython

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)

# The pins we'll use, each will have an internal pullup
keypress_pins = [board.D0, board.D1, board.D2, board.D3, board.D8, board.D9, board.SDA, board.SCL]
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [
                [ #button No1
                    [Keycode.LEFT_ARROW],
                ],
                [ #button No2
                    [Keycode.RIGHT_ARROW],
                ],
                [ #button No3
                    [Keycode.UP_ARROW],
                ],
                [ #button No4
                    [Keycode.DOWN_ARROW],
                ],
                [ #button No5
                    [Keycode.FIVE],
                    [Keycode.ENTER],
                ],
                [ #button No6
                    [Keycode.SIX],
                    [Keycode.ENTER],
                ],
                [ #button No7
                    [Keycode.SEVEN],
                    [Keycode.ENTER],
                ],
                [ #button No8
                    [Keycode.EIGHT],
                    [Keycode.ENTER],
                ]
               ]

# Make all pin objects inputs with pullups
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.direction = digitalio.Direction.INPUT
    key_pin.pull = digitalio.Pull.UP
    key_pin_array.append(key_pin)

# For Led
onboardled = digitalio.DigitalInOut(board.D10)
onboardled.direction = digitalio.Direction.OUTPUT
onboardled.value = False

print("Waiting for key pin...")

while True:
    # Check each pin
    for key_pin in key_pin_array:
        if not key_pin.value:  # Is it grounded?
            i = key_pin_array.index(key_pin)
            print("Pin #%d is grounded." % i)

            # Turn on the red LED
            onboardled.value = True

            while not key_pin.value:
                pass  # Wait for it to be ungrounded!
            # "Type" the Keycode
            key_array = keys_pressed[i]
            key_words_length = len(key_array)
            j = 0
            while j < key_words_length:
                key_length = len(key_array[j])
                if key_length == 2:
                    keyboard.press(key_array[j][0], key_array[j][1])
                elif key_length == 3:
                    keyboard.press(key_array[j][0], key_array[j][1], key_array[j][2])
                elif key_length == 4:
                    keyboard.press(key_array[j][0], key_array[j][1], key_array[j][2], key_array[j][3])
                elif key_length == 5:
                    keyboard.press(key_array[j][0], key_array[j][1], key_array[j][2], key_array[j][3], key_array[j][4])
                elif key_length == 6:
                    keyboard.press(key_array[j][0], key_array[j][1], key_array[j][2], key_array[j][3], key_array[j][4], key_array[j][5])
                else:
                    # key_length == 1
                    keyboard.press(key_array[j][0])

                keyboard.release_all()  # ..."Release"!
                j += 1

            # Turn off the red LED
            onboardled.value = False

    time.sleep(0.1)
