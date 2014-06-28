from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):

    def create_panda(self, name):
        self.manager.current = 'panda_screen'

    def create_doctor(self, name):
        self.manager.current = 'doctor_screen'
