from prac_09.car import Car
from random import *


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability = 50):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_driving_chance = randint(0, 100)

        if random_driving_chance < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            return distance

    def __str__(self):
        if self.odometer == 0:
            return f"{super().__str__()} {self.name} failed and did not move "
        else:
            return f"{super().__str__()}"
