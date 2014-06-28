from kivy.uix.screenmanager import Screen
from core import Doctor
from kivy.clock import Clock
from config import *


class DoctorScreen(Screen):
    def initialize(self):
        name = self.manager.get_screen('login_screen').ids.text_input.text
        self.doctor = Doctor(name)
        Clock.schedule_interval(self.make_hungry, HUNGER_TIME)
        Clock.schedule_interval(self.make_dirty, ClEAN_TIME)
        Clock.schedule_interval(self.make_sleep, SLEEP_TIME)
        Clock.schedule_interval(self.get_sick, 1)
        Clock.schedule_interval(self.calculate_happiness, 20)
        Clock.schedule_interval(self.update_labels, 0.1)
        Clock.schedule_interval(self.update_picture, 0.01)

    def make_hungry(self, dt):
        self.doctor.make_hungry()

    def make_dirty(self, dt):
        self.doctor.make_dirty()

    def make_sleep(self, dt):
        self.doctor.make_sleep()

    def get_sick(self, dt):
        self.doctor.get_sick()

    def calculate_happiness(self, dt):
        self.doctor.calculate_happiness()

    def doctor_pictures(self):
        if self.doctor.incarnation == 1:
            return './images/doctors/01.png'
        elif self.doctor.incarnation == 2:
            return './images/doctors/02.png'
        elif self.doctor.incarnation == 3:
            return './images/doctors/03.png'
        elif self.doctor.incarnation == 4:
            return './images/doctors/04.png'
        elif self.doctor.incarnation == 5:
            return './images/doctors/05.png'
        elif self.doctor.incarnation == 6:
            return './images/doctors/06.png'
        elif self.doctor.incarnation == 7:
            return './images/doctors/07.png'
        elif self.doctor.incarnation == 8:
            return './images/doctors/08.png'
        elif self.doctor.incarnation == 9:
            return './images/doctors/09.png'
        elif self.doctor.incarnation == 10:
            return './images/doctors/10.png'
        elif self.doctor.incarnation == 11:
            return './images/doctors/11.png'
        else:
            return './images/black_tile.png'

    def doctor_energy(self):
        return self.doctor.energy

    def doctor_health(self):
        return self.doctor.health

    def doctor_happiness(self):
        return self.doctor.happiness

    def doctor_clean(self):
        return self.doctor.clean

    def doctor_hunger(self):
        return self.doctor.hunger

    def feed_button(self):
        self.doctor.feed()

    def clear_button(self):
        self.doctor.clear()

    def heal_button(self):
        self.doctor.heal()

    def sleep_button(self):
        self.doctor.sleep()

    def play_button(self):
        self.manager.current = 'game_screen'

    def update_labels(self, dt):
        self.ids.energy_bar.text = 'Energy: ' + str(self.doctor_energy())
        self.ids.health_bar.text = 'Health: ' + str(self.doctor_health())
        self.ids.happiness_bar.text = 'Happiness: ' + str(self.doctor_happiness())
        self.ids.clean_bar.text = 'Clean: ' + str(self.doctor_clean())
        self.ids.hunger_bar.text = 'Hunger: ' + str(self.doctor_hunger())
        self.ids.doctor_name = self.doctor.name

    def update_picture(self, dt):
        self.ids.doctor_image.source = self.doctor_pictures()

    def stop_all_the_schedules(self):
        Clock.unschedule(self.make_hungry)
        Clock.unschedule(self.make_dirty)
        Clock.unschedule(self.make_sleep)
        Clock.unschedule(self.get_sick)
        Clock.unschedule(self.calculate_happiness)
        Clock.unschedule(self.update_labels)
        Clock.unschedule(self.update_picture)
