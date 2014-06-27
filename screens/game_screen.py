import itertools
import os
from random import choice

from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from core import ClickGame
from config import *


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
