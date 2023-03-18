from random import randrange
from device import sound_manager

closed_sound_options = ['./sounds/oh_dear_you_are_dead.wav']
slightly_open_sound_options = ['./sounds/oh_dear_you_are_dead.wav']
mostly_open_sound_options = ['./sounds/oh_dear_you_are_dead.wav']
open_sound_options = ['./sounds/oh_dear_you_are_dead.wav']


def make_closed_noise():
    play_random_sound(closed_sound_options)


def make_slightly_open_noise():
    play_random_sound(slightly_open_sound_options)


def make_mostly_open_noise():
    play_random_sound(mostly_open_sound_options)


def make_open_noise():
    play_random_sound(open_sound_options)


def play_random_sound(options):
    sound = randrange(0, len(options))
    sound_manager.play_sound(sound)
