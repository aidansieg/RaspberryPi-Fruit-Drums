# Aidan Siegel

import time
import board
import busio
import pygame

# Import MPR121 module.
import adafruit_mpr121

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

# Initialize pygame.
pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

# Initialize each sound to a variable and set volumes.
kick = pygame.mixer.Sound('samples/kick.wav')
kick.set_volume(.65);

snare = pygame.mixer.Sound('samples/snare.wav')
snare.set_volume(.65);

openhh = pygame.mixer.Sound('samples/open.wav')
openhh.set_volume(.65);

closedhh = pygame.mixer.Sound('samples/closed.wav')
closedhh.set_volume(.65);

clap = pygame.mixer.Sound('samples/clap.wav')
clap.set_volume(.65);

cymbal = pygame.mixer.Sound('samples/cymbal.wav')
cymbal.set_volume(.65);

# Loop forever testing each input and playing when they're touched.
while True:
    # Plays sound depending on which input gets touched.
    if mpr121[1].value:
        kick.play()

    elif mpr121[2].value:
        snare.play()

    elif mpr121[3].value:
        clap.play()

    elif mpr121[4].value:
        cymbal.play()

    elif mpr121[5].value:
        closedhh.play()

    elif mpr121[6].value:
        openhh.play()
