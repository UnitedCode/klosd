# Device runs python 3.9.2
from sounds import makeClosedNoise, makeMostlyOpenNoise, makeOpenNoise, makeSlightlyOpenNoise
from device import potentiometer
import threading


class Main():
    currentQuadrant = 0
    previousQuadrant = 0
    timer = None

    def run(self):
        while True:
            self.previousQuadrant = self.currentQuadrant
            self.currentQuadrant = self.getCurrentQuadrant()

            if not self.previousQuadrant == self.currentQuadrant:
                self.handleQuadrantChange()

    def handleQuadrantChange(self):
        # We've just moved, fiddle with timers, starting or killing them.
        if self.timer:
            self.timer.cancel()

        self.timer = self.startCountdown(3, self.makeNoise)
        # start a timer
        # if the timer goes off
        # run the loud code with the quadrant

        return

    def makeNoise(self):
        quadrantNoiseDict = {
            0: makeClosedNoise,
            1: makeSlightlyOpenNoise,
            2: makeMostlyOpenNoise,
            3: makeOpenNoise
        }
        quadrantNoiseDict[self.currentQuadrant]

    # return an int based on the closest fraction out of 4
    def getCurrentQuadrant(self):
        sensorValue = potentiometer.get_value()

        if sensorValue < 0.25:
            return 1
        elif sensorValue < 0.5:
            return 2
        elif sensorValue < 0.75:
            return 3
        else:
            return 4

    def startCountdown(self, seconds, callback):
        timer = threading.Timer(seconds, callback)
        timer.start()

        return timer


main = Main()
main.run()
