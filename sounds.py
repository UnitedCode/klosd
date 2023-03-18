from random import randrange
from device import sound_manager

closedSoundOptions = ['./sounds/oh_dear_you_are_dead.wav']
slightlyOpenSoundOptions = ['./sounds/oh_dear_you_are_dead.wav']
mostlyOpenSoundOptions = ['./sounds/oh_dear_you_are_dead.wav']
openSoundOptions = ['./sounds/oh_dear_you_are_dead.wav']

def makeClosedNoise():
    playRandomSound(closedSoundOptions)

def makeSlightlyOpenNoise():
    playRandomSound(slightlyOpenSoundOptions)

def makeMostlyOpenNoise():
    playRandomSound(mostlyOpenSoundOptions)

def makeOpenNoise():
    playRandomSound(openSoundOptions)

def playRandomSound(options):
    sound = randrange(0, len(options))
    sound_manager.play_sound(sound)