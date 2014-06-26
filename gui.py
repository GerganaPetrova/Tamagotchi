from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

from core import *

Builder.load_string(open('./tamagotchi.kv').read())

class PandaScreen(Screen):
    pass


class LoginScreen(Screen):

    def create_panda(self, name):
        screen_manager.current = 'panda_screen'

    def create_doctor(button, name):
        return Doctor(name)

screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name='login_screen'))
screen_manager.add_widget(PandaScreen(name='panda_screen'))
screen_manager.current = 'login_screen'

class TamagotchiApp(App):

    def build(self):
        return screen_manager

if __name__ == '__main__':
    TamagotchiApp().run()



