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

    def test_clear(self):
        self.tamagotchi.clear()
        self.assertEqual(self.tamagotchi.clean, 7)

    def test_full_clear(self):
        self.tamagotchi.clear()
        self.tamagotchi.clear()
        self.tamagotchi.clear()
        self.assertEqual(self.tamagotchi.clean, 10)

    def test_feed(self):
        self.tamagotchi.feed()
        self.assertEqual(self.tamagotchi.hunger, 7)

    def test_full_feed(self):
        self.tamagotchi.feed()
        self.tamagotchi.feed()
        self.tamagotchi.feed()
        self.assertEqual(self.tamagotchi.hunger, 10)

    def test_heal(self):
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi.health, 7)

    def test_full_heal(self):
        self.tamagotchi.heal()
        self.tamagotchi.heal()
        self.assertEqual(self.tamagotchi.health, 10)

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
        self.assertEqual(self.tamagotchi._health, 4)

    def test_get_full_sick(self):
        self.tamagotchi._clean = 2
        self.tamagotchi._hunger = 2
        self.tamagotchi._energy = 2
        self.tamagotchi.get_sick()

        self.assertEqual(self.tamagotchi.health, 3)


    def test_kill(self):
        self.tamagotchi.kill()
        self.assertFalse(self.tamagotchi.is_alive)

    def test_hunger_property(self):
        self.assertEqual(self.tamagotchi.hunger, 5)

    def test_energy_property(self):
        self.assertEqual(self.tamagotchi.energy, 5)

    def test_health_property(self):
        self.assertEqual(self.tamagotchi.health, 5)

    def test_happiness_property(self):
        self.assertEqual(self.tamagotchi.happiness, 5)

    def test_clean_property(self):
        self.assertEqual(self.tamagotchi.clean, 5)

if __name__ == '__main__':
    unittest.main()
