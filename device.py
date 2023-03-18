import time
import board
import busio
import subprocess
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class Potentiometer:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        self._max_voltage = 3.3
        self._samples = 10
        self._channel = AnalogIn(ads, ADS.P0)

    def get_value(self):
        value = 0
        for n in range(self._samples):
            value += self._channel.voltage / self._max_voltage
            time.sleep(0.02)

        return value / self._samples


class SoundManager:
    def play_sound(self, file):
        subprocess.Popen(['aplay', file])


potentiometer = Potentiometer()
sound_manager = SoundManager()

sound_manager.play_sound('./sounds/oh_dear_you_are_dead.wav')
