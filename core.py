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
        self._name = name
        self._energy = STARTING_ENERGY
        self._health = STARTING_HEALTH
        self._hunger = STARTING_HUNGER
        self._clean = STARTING_CLEAN
        self._happiness = STARTING_HAPPINESS

    def calculate_happiness(self):
        return (self._energy +  self._health
                + self._hunger + self._clean) / 4

    def feed(self, food):
        self.hunger += food.nutritive_value
        if self.hunger > MAX_HUNGER:
            self.hunger = MAX_HUNGER

    def heal(self):
        if self.health < MAX_HEALTH / 2:
            self.health += HEALTH_UPDATE
        else:
            self.health = MAX_HEALTH

    def clean(self):
        self.clean += CLEAN_UPDATE

    def get_sick(self):
        if self._clean < 3 and self._hunger < 3 and self._energy < 3:
            self._health -=  2


    def kill(self):
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

class ClickGame:

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


class Doctor(Tamagotchi):

    def __init__(self, name):
        Tamagotchi.__init__(self, name)
        incarnation = 1

    def kill(self):
        if number > 11:
            self.is_alive = False
        else:
            self.incarnation += 1
