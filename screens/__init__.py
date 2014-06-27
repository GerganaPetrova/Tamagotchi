from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.panda_screen import PandaScreen
from screens.game_screen import GameScreen
from screens.doctor_screen import DoctorScreen

def init_screen_manager():
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

    return screen_manager
