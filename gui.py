import itertools

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from random import choice
import os, sys
from core import *
from config import *

Builder.load_string(open('./tamagotchi.kv').read())


class DoctorScreen(Screen):
    pass

class LoginScreen(Screen):

    def create_panda(self, name):
        screen_manager.current = 'panda_screen'


    def create_doctor(button, name):
        screen_manager.current = 'doctor_screen'

class PandaScreen(Screen):
    def initialize(self):
        self.name = screens['login_screen'].ids.text_input.text
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

    def play_button(button):
        screen_manager.current = 'game_screen'

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

class GameScreen(Screen):
    def initialize(self):
        self.game = ClickGame(3, 3)
        self.picture = self.random_picture()
        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        if self.game.is_over:
            print(self.game.position)
            return False
        else:
            self.game.update()

            for box_layout in self.ids.game_grid.children:
                box_layout.children[0].source = './images/black_tile.png'

            self.ids['%dx%d' % (self.game.position)].source = self.picture
            print('KIL')

    def random_picture(self):
        pictures = os.listdir('./images/pandas/')
        random_picture = choice(pictures)
        return './images/pandas/' + random_picture

    def coordinate_transform(self, coordinates):
        IMG_WIDTH,IMG_HEIGHT = (135, 138)
        for x, y in itertools.product(range(3), range(3)):
            grid_element = self.ids['%dx%d' % (x, y)]
            relative_coordinates = grid_element.to_widget(*coordinates, relative=True)
            if (0 < relative_coordinates[0] < IMG_HEIGHT and
                0 < relative_coordinates[1] < IMG_WIDTH):
                return x, y

    def on_touch_down(self, touch):
        pos = self.coordinate_transform(touch.pos)
        if not pos:
            # evil bug :(
            return

        self.game.handle_touch(pos)
        self.update_score_display()

    def update_score_display(self):
        self.ids.points.text = str(self.game.points)
        self.ids.touch_counter = self.game.touch_counter


screen_manager = ScreenManager()
screens = {
    'login_screen': LoginScreen(name='login_screen'),
    'panda_screen': PandaScreen(name='panda_screen'),
    'doctor_screen': DoctorScreen(name='doctor_screen'),
    'game_screen': GameScreen(name='game_screen'),
}
screen_manager.add_widget(screens['login_screen'])
screen_manager.add_widget(screens['panda_screen'])
screen_manager.add_widget(screens['doctor_screen'])
screen_manager.add_widget(screens['game_screen'])


class TamagotchiApp(App):

    def build(self):
        return screen_manager

if __name__ == '__main__':
    TamagotchiApp().run()



