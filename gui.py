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
from kivy.properties import StringProperty
from core import *

Builder.load_string(open('./tamagotchi.kv').read())


class DoctorScreen(Screen):
    pass

class LoginScreen(Screen):

    name = StringProperty()

    def create_panda(self, name):
        name = name
        screen_manager.current = 'panda_screen'


    def create_doctor(button, name):
        doctor_name = name
        screen_manager.current = 'doctor_screen'

panda = Panda('Pencho')
class PandaScreen(Screen):

    def panda_energy(self):
        return panda.energy

    def panda_health(self):
        return panda.health

    def panda_happiness(self):
        return panda.happiness

    def panda_clean(self):
        return panda.clean

    def panda_hunger(self):
        return panda.hunger

screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name='login_screen'))
screen_manager.add_widget(PandaScreen(name='panda_screen'))
screen_manager.add_widget(DoctorScreen(name='doctor_screen'))

class TamagotchiApp(App):

    def build(self):
        return screen_manager

if __name__ == '__main__':
    TamagotchiApp().run()



