from machine import Pin
from time import sleep_ms

A = Pin(13, Pin.OUT)
B = Pin(12, Pin.OUT)
C = Pin(11, Pin.OUT)
D = Pin(10, Pin.OUT)

steps = [
    (1,0,0,0),
    (0,1,0,0),
    (0,0,0,1),
    (0,0,1,0)
]

while True:

    # forward
    for _ in range(400):
        for s in steps:
            A.value(s[0])
            B.value(s[1])
            C.value(s[2])
            D.value(s[3])
            sleep_ms(2)

    sleep_ms(500)

    # backward
    for _ in range(400):
        for s in reversed(steps):
            A.value(s[0])
            B.value(s[1])
            C.value(s[2])
            D.value(s[3])
            sleep_ms(2)

    sleep_ms(500)
