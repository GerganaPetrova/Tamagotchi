import unittest
import config
import core

class TestTamagotchi(unittest.TestCase):

    def setUp(self):
        self.tamagotchi = core.Tamagotchi('Test')

    def test_is_alive(self):
        self.assertTrue(self.tamagotchi.is_alive)

    def test_is_hungry(self):
        self.assertTrue(self.tamagotchi.is_hungry)

    def test_is_tired(self):
        self.assertTrue(self.tamagotchi.is_tired)

    def test_is_sad(self):
        self.assertTrue(self.tamagotchi.is_sad)

    def test_is_dirty(self):
        self.assertTrue(self.tamagotchi.is_dirty)

    def test_clean(self):
        self.tamagotchi.clean()
        self.assertEqual(self.tamagotchi._clean, 7)

    def test_full_clean(self):
        self.tamagotchi.clean()
        self.tamagotchi.clean()
        self.tamagotchi.clean()
        self.assertEqual(self.tamagotchi._clean, 10)

    def test_feed(self):
        self.tamagotchi.feed()
        self.assertEqual(self.tamagotchi._hunger, 7)

    def test_full_feed(self):
        self.tamagotchi.feed()
        self.tamagotchi.feed()
        self.tamagotchi.feed()
        self.assertEqual(self.tamagotchi._hunger, 10)

    def test_heal(self):
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi._health, 7)

    def test_full_heal(self):
        self.tamagotchi.heal()
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi._health, 10)


    def test_calculate_strarting_happiness(self):
        self.assertEqual(self.tamagotchi._happiness, self.tamagotchi.calculate_happiness())

    def test_calculate_happiness(self):
        self.tamagotchi._energy = 10
        self.tamagotchi._health = 5
        self.tamagotchi._hunger = 5
        self.tamagotchi._clean = 0

        self.assertEqual(self.tamagotchi.calculate_happiness(), 5)


    def test_get_sick(self):
        self.tamagotchi.get_sick()
        self.assertEqual(self.tamagotchi._health, 4)

    def test_get_full_sick(self):
        self.tamagotchi._clean = 2
        self.tamagotchi._hunger = 2
        self.tamagotchi._energy = 2
        self.tamagotchi.get_sick()

        self.assertEqual(self.tamagotchi._health, 3)


    def test_kill(self):
        self.tamagotchi.kill()
        self.assertFalse(self.tamagotchi.is_alive)


if __name__ == '__main__':
    unittest.main()
