import unittest

from .utils import check_validity
from src.tank import Tank

class TestTank(unittest.TestCase):

    def test_set(self):
        # Arrange
        t1 = Tank("t1", 100, level=10)

        # Act

        # Assert
        self.assertEqual(t1.level, 10)
        self.assertEqual(t1.max, 100)
        self.assertEqual(t1.name, "t1")

    def test_level(self):
        # Arrange
        t1 = Tank("t1", 100, level=10)
        t2 = Tank("t2", 100, level=20)
        
        # Act
        t1.move_to(t2, 10)
        
        # Assert
        self.assertEqual(t1.level, 0)
        self.assertEqual(t2.level, 30)

    def test_validity(self):
        # Arrange
        tanks: list[Tank] = [Tank('t'+str(i), 100, level=i*10) for i in range(1, 10)]

        # Act
        # t1 -> t9
        # t2 -> t8
        # t3 -> t7
        # t4 -> t6
        for s, e in zip(range(0, 5), range(8, 4, -1)):
            tanks[s].move_to(tanks[e], tanks[s].level)

        # Assert
        self.assertIs(check_validity(tanks, 450), True)

if __name__ == "__main__":
    unittest.main()