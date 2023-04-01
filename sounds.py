from random import randrange
from device import sound_manager

closed_sound_options = ['./sounds/PassiveAgressive.wav','./sounds/AAAaaaAAAAaaaaaAAaaAAaaaAaahhhhHHHhh.wav', './sounds/IAmInPain.wav']
slightly_open_sound_options = ['./sounds/RaisedInABarn.wav', './sounds/LibralSissies.wav', './sounds/ShutMeOutTake.wav']
mostly_open_sound_options = ['./sounds/stfd.wav', './sounds/WasThatSoHard.wav']
open_sound_options = ['./sounds/WifeAndKids.wav', './sounds/thx.wav']


def make_closed_noise():
    play_random_sound(closed_sound_options)


def make_slightly_open_noise():
    play_random_sound(slightly_open_sound_options)


def make_mostly_open_noise():
    play_random_sound(mostly_open_sound_options)


def make_open_noise():
    play_random_sound(open_sound_options)


def play_random_sound(options):
    sound = options[randrange(0, len(options))]
    sound_manager.play_sound(sound)
