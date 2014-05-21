from kivy import clock

class Food:

    def __init__(self, name, nutritive_value):
        self.name = name
        self.nutritive_value = nutritive_value


class Tamagotchi:

    def __init__(self, name):
        self.name = 5
        self._energy = 5
        self._happy = 5
        self._health = 5
        self._hunger = 5
        self._clarity = 5

    def feed(self, food):
        self.hunger += food.nutritive_value
        if self.hunger > 10:
            self.hunger = 10

    def heal(self):
        if self.heal < 5:
            self.health += 2
        else:
            self.health = 10

    def clean(self):
        self.clarity += 2

    def is_hungry(self):
        return self._hunger < 10

    def is_tired(self):
        return self._energy < 10

    def is_sad(self):
        return self._happy < 10

    def is_sick(self):
        return self._health < 10

    def is_dirty(self):
        return self._clarity < 10


    def state(self):
        tamagotchi_state = {
            'tired':  self.is_tired(),
            'hungry': self.is_hungry(),
            'sad':    self.is_sad(),
            'sick':   self.is_sick(),
            'dirty':  self.is_dirty(),
        }
        return tamagotchi_state
