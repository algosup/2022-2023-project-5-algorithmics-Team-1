import unittest

from .helper import check_validity
from src.tank import Tank
from decimal import Decimal as Dec

class TestTank(unittest.TestCase):

    def test_set(self):
        # Arrange
        t1 = Tank("t1", 100, flevel=10)

        # Act

        # Assert
        self.assertEqual(t1.level, 10)
        self.assertEqual(t1.max, 100)
        self.assertEqual(t1.name, "t1")

    def test_set_negative(self):
        # Arrange
        t1 = Tank("t1", 100, flevel=-10)

        # Act

        # Assert
        self.assertEqual(t1.level, -10)
        self.assertEqual(t1.max, 100)
        self.assertEqual(t1.name, "t1")

    def test_set_over_max(self):
        # Arrange

        # Act

        # Assert
        self.assertRaises(ValueError, Tank,"t1", 100, flevel=210)

    def test_set_character(self):
            # Arrange

            # Act

            # Assert
            self.assertRaises(TypeError, Tank,"t1", 100, flevel="a")

    def test_level(self):
        # Arrange
        t1 = Tank("t1", 100, flevel=10)
        t2 = Tank("t2", 100, flevel=20)
        
        # Act
        t1.move_unit_to(t2, 10)
        
        # Assert
        self.assertEqual(t1.level, Dec(0))
        self.assertEqual(t2.level, Dec(30))

    def test_level_negative(self):
        # Arrange
        t1 = Tank("t1", 100, flevel=10)
        t2 = Tank("t2", 100, flevel=20)
        
        # Act
        
        # Assert
        self.assertRaises(ValueError,t1.move_unit_to,t2, -10)
    
    # def test_level_character(self):
    #     # Arrange
    #     t1 = Tank("t1", 100, flevel=10)
    #     t2 = Tank("t2", 100, flevel=20)
        
    #     # Act
        
    #     # Assert
        # self.assertRaises(TypeError,t1.move_unit_to,t2, "a")

    def test_move_unit_to__not_enough_in_self(self):
        self.assertRaises(ValueError, Tank("t1", 100, flevel=10).move_unit_to, Tank("t2", 100, flevel=0), 20)
        
    def test_move_unit_to__no_space_in_target(self):
        self.assertRaises(ValueError, Tank("t1", 100, flevel=10).move_unit_to, Tank("t2", 100, flevel=100), 10)

    def test_validity(self):
        # Arrange
        tanks: list[Tank] = [Tank('t'+str(i), 100, flevel=i*10) for i in range(1, 10)]

        # Act
        # t1 -> t9
        # t2 -> t8
        # t3 -> t7
        # t4 -> t6
        for s, e in zip(range(0, 5), range(8, 4, -1)):
            tanks[s].move_unit_to(tanks[e], tanks[s].level)

        # Assert
        self.assertIs(check_validity(tanks, 450), True)

if __name__ == "__main__":
    unittest.main()