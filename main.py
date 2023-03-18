# Device runs python 3.9.2
from sounds import make_closed_noise, make_mostly_open_noise, make_open_noise, make_slightly_open_noise
from device import potentiometer
import threading


class Main():
    current_quadrant = 0
    previous_quadrant = 0
    timer = None

    def run(self):
        while True:
            self.previous_quadrant = self.current_quadrant
            self.current_quadrant = self.get_current_quadrant()

            if not self.previous_quadrant == self.current_quadrant:
                self.handle_quadrant_change()

    def handle_quadrant_change(self):
        # We've just moved, fiddle with timers, starting or killing them.
        if self.timer:
            self.timer.cancel()

        self.timer = self.start_countdown(3, self.make_noise)
        # start a timer
        # if the timer goes off
        # run the loud code with the quadrant

        return

    def make_noise(self):
        quadrant_mapping = {
            0: make_closed_noise,
            1: make_slightly_open_noise,
            2: make_mostly_open_noise,
            3: make_open_noise
        }
        
        quadrant_mapping[self.current_quadrant - 1]()

    # return an int based on the closest fraction out of 4
    def get_current_quadrant(self):
        sensor_value = potentiometer.get_value()

        if sensor_value < 0.25:
            return 1
        elif sensor_value < 0.5:
            return 2
        elif sensor_value < 0.75:
            return 3
        else:
            return 4

    def start_countdown(seconds, callback):
        timer = threading.Timer(seconds, callback)
        timer.start()

        return timer


main = Main()
main.run()
