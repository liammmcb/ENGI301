# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3 LED
--------------------------------------------------------------------------
License:   
Copyright 2024 - <Liam McConnico-Blanchet>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

File that will blink USR3 LED at chosen frequency
    - initial frequency will be 5Hz


--------------------------------------------------------------------------
"""

import Adafruit_BBIO.GPIO as GPIO
import time

USR3 = "USR3"
GPIO.setup(USR3, GPIO.OUT)

    # If I want to add another LED outputs, just follow the same process and 
    # remember to setup the LED with GPIO.OUT

try:
    while True:
        GPIO.output("USR3", GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output("USR3", GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output("USR3", GPIO.LOW)
    pass

GPIO.cleanup()