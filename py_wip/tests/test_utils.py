import unittest

from src.tank import Tank
from src.utils import theoretical_max

class TestUtils(unittest.TestCase):

    def test_set(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=80),
        ]
        formula = "25%t1+50%t2+12.5%t3+12.5%t4"

        # Act
        maximum = theoretical_max(tanks, formula)

        # Assert
        self.assertEqual(maximum, 150)

if __name__ == "__main__":
    unittest.main()