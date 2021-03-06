from kivy import clock
from config import *
from random import randint


class Tamagotchi:

    def __init__(self, name):
        self._is_alive = True
        self._name = name
        self._energy = MAX_ENERGY
        self._health = MAX_HEALTH
        self._hunger = MAX_HUNGER
        self._clean = MAX_CLEAN
        self._happiness = MAX_HAPPINESS

    @property
    def name(self):
        return self._name

    @property
    def energy(self):
        return self._energy

    @property
    def health(self):
        return self._health

    @property
    def hunger(self):
        return self._hunger

    @property
    def clean(self):
        return self._clean

    @property
    def happiness(self):
        return self._happiness

    def calculate_happiness(self):
        return (self._energy + self._health
                + self._hunger + self._clean) / 4

    def feed(self):
        self._hunger += HUNGER_UPDATE
        if self._hunger > MAX_HUNGER:
            self._hunger = MAX_HUNGER

    def heal(self):
        if self._health <= MAX_HEALTH / 2:
            self._health += HEALTH_UPDATE
        else:
            self._health = MAX_HEALTH

    def clear(self):
        self._clean += CLEAN_UPDATE
        if self._clean > MAX_CLEAN:
            self._clean = MAX_CLEAN

    def sleep(self):
        self._energy = MAX_ENERGY

    def get_sick(self):
        if self._health <= 0:
            self._is_alive = False
        else:
            self._health -= HEALTH_UPDATE

    def make_hungry(self):
        if self._hunger >= 1:
            self._hunger -= HUNGER_UPDATE

    def make_dirty(self):
        if self._clean >= 1:
            self._clean -= CLEAN_UPDATE

    def make_sleep(self):
        if self._energy >= 1:
            self._energy -= ENERGY_UPDATE

    @property
    def is_hungry(self):
        return self._hunger < MAX_HUNGER / 2

    @property
    def is_tired(self):
        return self._energy < MAX_ENERGY / 2

    @property
    def is_sad(self):
        return self.calculate_happiness() < MAX_HAPPINESS / 2

    @property
    def is_sick(self):
        return self._health < MAX_HEALTH / 2

    @property
    def is_dirty(self):
        return self._clean < MAX_CLEAN / 2

    @property
    def is_alive(self):
        return self._is_alive


class ClickGame:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.touch_counter = 0
        self.points = 0

    @property
    def is_over(self):
        return self.touch_counter >= GAME_MAX_MOVES

    def start(self):
        self.update()

    def handle_touch(self, coordinates):
        if coordinates[0] in range(0, self.width)\
           and coordinates[1] in range(0, self.height):
            self.touch_counter += 1

            if self.is_correct(coordinates):
                self.points += 1
        else:
            raise TypeError("Out of board")

    def is_correct(self, coordinates):
        return self.position == coordinates

    def update(self):
        self.position = (
            randint(0, self.width - 1),
            randint(0, self.height - 1)
        )


class Panda(Tamagotchi):

    def __init__(self, name):
        Tamagotchi.__init__(self, name)


class Doctor(Tamagotchi):

    def __init__(self, name):
        Tamagotchi.__init__(self, name)
        self._incarnation = 1

    @property
    def incarnation(self):
        return self._incarnation

    def get_sick(self):
        if self._health <= 0:
            self.kill()
            self._health = MAX_HEALTH
        else:
            self._health -= HEALTH_UPDATE

    def kill(self):
        if self.incarnation > 11:
            self.is_alive = False
        else:
            self._incarnation += 1
