from kivy.uix.screenmanager import Screen
from core import Panda
from kivy.clock import Clock
from config import *

class PandaScreen(Screen):
    def initialize(self):
        self.name = self.manager.get_screen('login_screen').ids.text_input.text
        self.panda = Panda(self.name)
        Clock.schedule_interval(self.make_hungry, HUNGER_TIME)
        Clock.schedule_interval(self.make_dirty, ClEAN_TIME)
        Clock.schedule_interval(self.make_sleep, SLEEP_TIME)
        Clock.schedule_interval(self.get_sick, 60)
        Clock.schedule_interval(self.calculate_happiness, 20)
        Clock.schedule_interval(self.update_labels, 0.1)
        Clock.schedule_interval(self.update_picture, 0.01)


    def make_hungry(self, dt):
        self.panda.make_hungry()

    def make_dirty(self, dt):
        self.panda.make_dirty()

    def make_sleep(self, dt):
        self.panda.make_sleep()

    def get_sick(self, dt):
        self.panda.get_sick()

    def calculate_happiness(self, dt):
        self.panda.calculate_happiness()


    def panda_pictures(self):
        if not self.panda.is_alive:
            return './images/pandas/dead_panda.png'
        elif self.panda.is_hungry:
            return './images/pandas/panda_hungry.png'
        elif self.panda.is_sick:
            return './images/pandas/pandas19.png'
        elif self.panda.is_dirty:
            return './images/pandas/panda_dirty.png'
        elif self.panda.is_sad:
            return './images/pandas/pandas29.png'
        elif self.panda.is_tired:
            return './images/pandas/panda_tired.png'
        else:
            return './images/pandas/panda.png'

    def panda_energy(self):
        return self.panda.energy

    def panda_health(self):
        return self.panda.health

    def panda_happiness(self):
        return self.panda.happiness

    def panda_clean(self):
        return self.panda.clean

    def panda_hunger(self):
        return self.panda.hunger

    def feed_button(self):
        self.panda.feed()

    def clear_button(self):
        self.panda.clear()

    def heal_button(self):
        self.panda.heal()

    def sleep_button(self):
        self.panda.sleep()

    def play_button(self):
        self.manager.current = 'game_screen'

    def update_labels(self, dt):
        self.ids.energy_bar.text = 'Energy: ' + str(self.panda_energy())
        self.ids.health_bar.text = 'Health: ' + str(self.panda_health())
        self.ids.happiness_bar.text = 'Happiness: ' + str(self.panda_happiness())
        self.ids.clean_bar.text = 'Clean: ' +str(self.panda_clean())
        self.ids.hunger_bar.text = 'Hunger: ' + str(self.panda_hunger())

    def update_picture(self, dt):
        self.ids.panda_image.source = self.panda_pictures()

    def stop_all_the_schedules(self):
        Clock.unschedule(self.make_hungry)
        Clock.unschedule(self.make_dirty)
        Clock.unschedule(self.make_sleep)
        Clock.unschedule(self.get_sick)
        Clock.unschedule(self.calculate_happiness)
        Clock.unschedule(self.update_labels)
        Clock.unschedule(self.update_picture)
