import unittest
import config
import core


class TestTamagotchi(unittest.TestCase):

    def setUp(self):
        self.tamagotchi = core.Tamagotchi('Test')

    def test_is_alive(self):
        self.assertTrue(self.tamagotchi.is_alive)

    def test_is_hungry(self):
        self.assertFalse(self.tamagotchi.is_hungry)

    def test_is_tired(self):
        self.assertFalse(self.tamagotchi.is_tired)

    def test_is_sad(self):
        self.assertFalse(self.tamagotchi.is_sad)

    def test_is_dirty(self):
        self.assertFalse(self.tamagotchi.is_dirty)

    def test_make_dirty(self):
        self.tamagotchi.make_dirty()
        self.assertEqual(self.tamagotchi.clean, 19)

    def test_full_clear(self):
        self.tamagotchi.make_dirty()
        self.tamagotchi.make_dirty()
        self.tamagotchi.clear()
        self.tamagotchi.clear()
        self.assertEqual(self.tamagotchi.clean, 20)

    def test_make_hungry(self):
        self.tamagotchi.make_hungry()
        self.assertEqual(self.tamagotchi.hunger, 19)

    def test_full_feed(self):
        self.tamagotchi.make_hungry()
        self.tamagotchi.make_hungry()
        self.tamagotchi.feed()
        self.tamagotchi.feed()
        self.assertEqual(self.tamagotchi.hunger, 20)

    def test_heal(self):
        self.tamagotchi.get_sick()
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi.health, 20)

    def test_full_heal(self):
        self.tamagotchi._health = 11
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi.health, 20)

    def test_sleep(self):
        self.tamagotchi.sleep()
        self.assertFalse(self.tamagotchi.is_tired)

    def test_calculate_strarting_happiness(self):
        self.assertEqual(self.tamagotchi.happiness,
                         self.tamagotchi.calculate_happiness())

    def test_calculate_happiness(self):
        self.tamagotchi._energy = 10
        self.tamagotchi._health = 5
        self.tamagotchi._hunger = 5
        self.tamagotchi._clean = 0

        self.assertEqual(self.tamagotchi.calculate_happiness(), 5)

    def test_get_sick(self):
        self.tamagotchi.get_sick()
        self.assertEqual(self.tamagotchi._health, 19)

    def test_get_full_sick(self):
        self.tamagotchi._health = 0
        self.tamagotchi.get_sick()

        self.assertFalse(self.tamagotchi.is_alive)

    def test_hunger_property(self):
        self.assertEqual(self.tamagotchi.hunger, 20)

    def test_energy_property(self):
        self.assertEqual(self.tamagotchi.energy, 20)

    def test_health_property(self):
        self.assertEqual(self.tamagotchi.health, 20)

    def test_happiness_property(self):
        self.assertEqual(self.tamagotchi.happiness, 20)

    def test_clean_property(self):
        self.assertEqual(self.tamagotchi.clean, 20)


class TestClickGame(unittest.TestCase):

    def setUp(self):
        self.click_game = core.ClickGame(3, 3)

    def test_begin_touch_counter(self):
        self.assertEqual(self.click_game.touch_counter, 0)

    def test_begin_points(self):
        self.assertEqual(self.click_game.points, 0)

    def test_start(self):
        self.click_game.update()
        self.assertNotEqual(self.click_game.position, (None, None))

    def test_handle_touch(self):
        coordinates = (0, 2)
        self.click_game.position = coordinates
        handle_touch = self.click_game.handle_touch(coordinates)
        self.assertEqual(self.click_game.points, 1)

if __name__ == '__main__':
    unittest.main()
