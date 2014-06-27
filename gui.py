import itertools

from kivy.app import App
from kivy.lang import Builder
from random import choice
import os, sys
import screens
from core import *
from config import *

Builder.load_string(open('./tamagotchi.kv').read())

screen_manager = screens.init_screen_manager()

class TamagotchiApp(App):
    def build(self):
        return screen_manager


if __name__ == '__main__':
    TamagotchiApp().run()



