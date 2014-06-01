from kivy import clock
from config import *
from random import randint

class Food:

    def __init__(self, name, nutritive_value):
        self.name = name
        self.nutritive_value = nutritive_value


class Tamagotchi:

    def __init__(self, name):
        self._is_alive = True
        self.name = name
        self._energy = STARTING_ENERGY
        self._health = STARTING_HEALTH
        self._hunger = STARTING_HUNGER
        self._clean = STARTING_CLEAN
        self._happiness = STARTING_HAPPINESS

    def _calculate_happiness(self):
        return (self._energy + self._play + self._health
                + self._hunger + self._clarity) / 5

    def _feed(self, food):
        self.hunger += food.nutritive_value
        if self.hunger > MAX_HUNGER
            self.hunger = MAX_HUNGER

    def _heal(self):
        if self.health < MAX_HEALTH / 2:
            self.health += HEALTH_UPDATE
        else:
            self.health = MAX_HEALTH

    def _clean(self):
        self.clean += CLEAN_UPDATE

    def _kill(self):
        self._is_alive = False

    @property
    def is_hungry(self):
        return self._hunger < MAX_HUNGER

    @property
    def is_tired(self):
        return self._energy < MAX_ENERGY

    @property
    def is_sad(self):
        return self._calculate_happiness < MAX_HAPPINESS

    @property
    def is_sick(self):
        return self._health < MAX_HEALTH

    @property
    def is_dirty(self):
        return self._clean < MAX_CLEAN

    @property
    def is_alive(self):
        return self._is_alive

class PandaGame:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.touch_counter = 0

    def start(self):
        self.position = (randint(0, self.width), randint(0, self.height))

    def hadle_touch(self, coordinates):
        if coordinates[0] in range(0, self.width)\
           and coordinates[1] in range(0, self.height):
            self.touch_counter += 1
        raise TypeError("Out of board")

    def is_correct(self, coordinates):
        return self.position == coordinates


    def update(self):
        self.position = (randint(0, self.width), randint(0, self.height))


class Panda(Tamagotchi):

    def __init__(self, name):
        Tamagotchi.__init__(self, name)

    def play(self):
        pass


