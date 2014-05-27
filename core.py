from kivy import clock
from config import *

class Food:

    def __init__(self, name, nutritive_value):
        self.name = name
        self.nutritive_value = nutritive_value


class Tamagotchi:

    def __init__(self, name):
        self._is_alive = True
        self.name = name
        self._energy = STARTING_ENERGY
        self._play = STARTING_PLAY
        self._health = STARTING_HEALTH
        self._hunger = STARTING_HUNGER
        self._clarity = STARTING_CLARITY
        self._happiness = self._calculate_happiness()


    def _calculate_happiness(self):
        return (self._energy + self._play + self._health
                + self._hunger + self._clarity) / 5

    def _feed(self, food):
        self.hunger += food.nutritive_value
        if self.hunger > HUNGER:
            self.hunger = HUNGER

    def _heal(self):
        if self.health < HEALTH / 2:
            self.health += HEALTH_UPDATE
        else:
            self.health = HEALTH

    def _clean(self):
        self.clarity += CLARITY_UPDATE

    def _kill(self):
        self._is_alive = False

    @property
    def is_hungry(self):
        return self._hunger < HUNGER

    @property
    def is_tired(self):
        return self._energy < ENERGY

    @property
    def is_sad(self):
        return self._play < PLAY

    @property
    def is_sick(self):
        return self._health < HEALTH

    @property
    def is_dirty(self):
        return self._clarity < CLARITY

    @property
    def is_alice(self):
        return self._is_alive

    def state(self):
        tamagotchi_state = {
            'tired':  self.is_tired,
            'hungry': self.is_hungry,
            'sad':    self.is_sad,
            'sick':   self.is_sick,
            'dirty':  self.is_dirty,
            'alive':  self.is_alive,
        }
        return tamagotchi_state



class Panda(Tamagotchi):

    def __init__(self, name):
        Tamagotchi.__init__(self, name)


    def play(self):
        pass


