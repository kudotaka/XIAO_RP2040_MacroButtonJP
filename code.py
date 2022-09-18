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
import neopixel
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keycode_jp import KeycodeJP

# A simple neat keyboard demo in CircuitPython

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)

# The pins we'll use, each will have an internal pullup
keypress_pins = [board.D0]
# Our array of key objects
key_pin_array = []
# The Keycode sent for each button, will be paired with a control key
keys_pressed = [
                [ #button No1
                    [Keycode.A],
                    [Keycode.B],
                    [Keycode.C],
                    [Keycode.D],
                    [Keycode.E],
                    [Keycode.F],
                    [Keycode.G],
                    [Keycode.H],
                    [Keycode.I],
                    [Keycode.J],
                    [Keycode.K],
                    [Keycode.L],
                    [Keycode.M],
                    [Keycode.N],
                    [Keycode.O],
                    [Keycode.P],
                    [Keycode.Q],
                    [Keycode.R],
                    [Keycode.S],
                    [Keycode.T],
                    [Keycode.U],
                    [Keycode.V],
                    [Keycode.W],
                    [Keycode.X],
                    [Keycode.Y],
                    [Keycode.Z],
                    [Keycode.ENTER],
                    [Keycode.A, Keycode.SHIFT],
                    [Keycode.B, Keycode.SHIFT],
                    [Keycode.C, Keycode.SHIFT],
                    [Keycode.D, Keycode.SHIFT],
                    [Keycode.E, Keycode.SHIFT],
                    [Keycode.F, Keycode.SHIFT],
                    [Keycode.G, Keycode.SHIFT],
                    [Keycode.H, Keycode.SHIFT],
                    [Keycode.I, Keycode.SHIFT],
                    [Keycode.J, Keycode.SHIFT],
                    [Keycode.K, Keycode.SHIFT],
                    [Keycode.L, Keycode.SHIFT],
                    [Keycode.M, Keycode.SHIFT],
                    [Keycode.N, Keycode.SHIFT],
                    [Keycode.O, Keycode.SHIFT],
                    [Keycode.P, Keycode.SHIFT],
                    [Keycode.Q, Keycode.SHIFT],
                    [Keycode.R, Keycode.SHIFT],
                    [Keycode.S, Keycode.SHIFT],
                    [Keycode.T, Keycode.SHIFT],
                    [Keycode.U, Keycode.SHIFT],
                    [Keycode.V, Keycode.SHIFT],
                    [Keycode.W, Keycode.SHIFT],
                    [Keycode.X, Keycode.SHIFT],
                    [Keycode.Y, Keycode.SHIFT],
                    [Keycode.Z, Keycode.SHIFT],
                    [Keycode.ENTER],
                    [Keycode.ONE],
                    [Keycode.TWO],
                    [Keycode.THREE],
                    [Keycode.FOUR],
                    [Keycode.FIVE],
                    [Keycode.SIX],
                    [Keycode.SEVEN],
                    [Keycode.EIGHT],
                    [Keycode.NINE],
                    [Keycode.ZERO],
                    [Keycode.ENTER],
                    [Keycode.ONE, Keycode.SHIFT],
                    [Keycode.TWO, Keycode.SHIFT],
                    [Keycode.THREE, Keycode.SHIFT],
                    [Keycode.FOUR, Keycode.SHIFT],
                    [Keycode.FIVE, Keycode.SHIFT],
                    [Keycode.SIX, Keycode.SHIFT],
                    [Keycode.SEVEN, Keycode.SHIFT],
                    [Keycode.EIGHT, Keycode.SHIFT],
                    [Keycode.NINE, Keycode.SHIFT],
                    [Keycode.ENTER],
                    [KeycodeJP.MINUS],
                    [KeycodeJP.CIRCUMFLEX],
                    [KeycodeJP.INTERNATIONAL3],
                    [KeycodeJP.ATSIGN],
                    [KeycodeJP.LEFT_BRACKET],
                    [KeycodeJP.SEMICOLON],
                    [KeycodeJP.COLON],
                    [KeycodeJP.RIGHT_BRACKET],
                    [KeycodeJP.COMMA],
                    [KeycodeJP.PERIOD],
                    [KeycodeJP.FORWARD_SLASH],
                    [KeycodeJP.INTERNATIONAL1],
                    [Keycode.ENTER],
                    [KeycodeJP.MINUS, Keycode.SHIFT],
                    [KeycodeJP.CIRCUMFLEX, Keycode.SHIFT],
                    [KeycodeJP.INTERNATIONAL3, Keycode.SHIFT],
                    [KeycodeJP.ATSIGN, Keycode.SHIFT],
                    [KeycodeJP.LEFT_BRACKET, Keycode.SHIFT],
                    [KeycodeJP.SEMICOLON, Keycode.SHIFT],
                    [KeycodeJP.COLON, Keycode.SHIFT],
                    [KeycodeJP.RIGHT_BRACKET, Keycode.SHIFT],
                    [KeycodeJP.COMMA, Keycode.SHIFT],
                    [KeycodeJP.PERIOD, Keycode.SHIFT],
                    [KeycodeJP.FORWARD_SLASH, Keycode.SHIFT],
                    [KeycodeJP.INTERNATIONAL1, Keycode.SHIFT],
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
onboardled = digitalio.DigitalInOut(board.LED_BLUE)
onboardled.direction = digitalio.Direction.OUTPUT
onboardled.value = True

# For Pixel
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
pixel_onboard_pin = board.NEOPIXEL
num_onboard_pixels = 1
onboardpixels = neopixel.NeoPixel(pixel_onboard_pin, num_onboard_pixels, brightness=0.3, auto_write=False)
onboardpixels.fill(BLACK)
onboardpixels.show()

pixel_pin = board.D1
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
pixels.fill(BLACK)
pixels.show()

print("Waiting for key pin...")

while True:
    # Check each pin
    for key_pin in key_pin_array:
        if not key_pin.value:  # Is it grounded?
            i = key_pin_array.index(key_pin)
            print("Pin #%d is grounded." % i)

            # Turn on the red LED
            onboardled.value = False
            onboardpixels.fill(BLUE)
            onboardpixels.show()
            pixels.fill(BLUE)
            pixels.show()

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
            onboardled.value = True
            onboardpixels.fill(BLACK)
            onboardpixels.show()
            pixels.fill(BLACK)
            pixels.show()

    time.sleep(0.01)
