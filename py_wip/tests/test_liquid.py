import unittest

from src.liquid import Liquid

EPSILON = 0.00000000001

class TestLiquid(unittest.TestCase):

    def test_mod_simple(self):
        # Arrange
        l1_startlevel = 10
        l1 = Liquid("l1", l1_startlevel)
        l2_startlevel = 564
        l2 = Liquid("l2", l2_startlevel)

        # Act
        remaining1 = l1 % 0.5
        remaining2 = l2 % 0.3

        # Assert
        self.assertEqual(l1.level, l1_startlevel / 2)
        self.assertEqual(remaining1.level, l1_startlevel / 2)

        self.assertAlmostEqual(l2.level, l2_startlevel * 0.7, delta=EPSILON)
        self.assertAlmostEqual(remaining2.level, l2_startlevel * 0.3, delta=EPSILON)

    def test_truediv_simple(self):
        # Arrange
        l1_startlevel = 10
        l1 = Liquid("l1", l1_startlevel)
        l2_startlevel = 564
        l2 = Liquid("l2", l2_startlevel)

        # Act
        remaining1 = l1 / 2
        remaining2 = l2 / 3

        # Assert
        self.assertEqual(l1.level, l1_startlevel / 2)
        self.assertEqual(remaining1.level, l1_startlevel / 2)

        self.assertAlmostEqual(l2.level, l2_startlevel / 3, delta=EPSILON)
        self.assertAlmostEqual(remaining2.level, l2_startlevel - (l2_startlevel / 3), delta=EPSILON)

if __name__ == "__main__":
    unittest.main()