from random import randrange
from device import sound_manager

closedSoundOptions = ['/path/note.wav','/path/note2.wav', '/path/note3.wav']
slightlyOpenSoundOptions = ['/path/note.wav','/path/note2.wav', '/path/note3.wav']
mostlyOpenSoundOptions = ['/path/note.wav','/path/note2.wav', '/path/note3.wav']
openSoundOptions = ['/path/note.wav','/path/note2.wav', '/path/note3.wav']

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