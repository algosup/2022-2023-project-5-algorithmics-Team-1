import unittest

from src.liquid import Liquid
from src.tank import Tank
from src.utils import _number_to_percentage, _percentage_to_number, check_tank_formula, theoretical_max , get_min_level, get_name_from_tanks, create_nodes, get_tanks_with_nodes, aggregate ,remove_useless_tanks

class TestUtils(unittest.TestCase):

    def test_theorical_max(self):
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

    def test_number_to_percentage(self):
        # Arrange
        number = 90
        total = 180

        # Act
        percentage = _number_to_percentage(number, total)

        # Assert
        self.assertEqual(percentage, 50)

    def test_percentage_to_number(self):
        # Arrange
        percentage = 50
        total = 180

        # Act
        number = _percentage_to_number(percentage, total)

        # Assert
        self.assertEqual(number, 90)

    def test_get_min_level(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=80),
        ]

        # Act
        minimum = get_min_level(tanks)

        # Assert
        self.assertEqual(minimum, 25)

    def test_get_name_from_tanks(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=80),
        ]

        # Act
        name = get_name_from_tanks(tanks)

        # Assert
        self.assertEqual(name, "1,2,3,4")

    def test_create_nodes(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=0),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=0),
        ]

        # Act
        create_nodes(tanks)

        # Assert
        self.assertEqual(tanks[0].nodes, [])
        self.assertEqual(tanks[1].nodes, [tanks[0], tanks[3]])
        self.assertEqual(tanks[2].nodes, [tanks[0], tanks[3]])
        self.assertEqual(tanks[3].nodes, [])
    
    def test_get_tanks_with_nodes(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=0),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=0),
        ]

        # Act
        create_nodes(tanks)
        list = get_tanks_with_nodes(tanks)

        # Assert
        self.assertEqual(list, [tanks[1], tanks[2]])

    def test_aggregate(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=0),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=0),
        ]
        formula = [(0.25,"t1"),(0.5,"t2"),(0.25,"t3")]
        # Act
        list = aggregate(tanks,formula)

        # Assert
        self.assertEqual(list, [(0.25,tanks[0]), (0.5,tanks[1]), (0.25,tanks[2])])

    def test_remove_useless_tanks(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=0),
            Tank("t5", 150, level=0),
            Tank("t6", 95, level=95),
            Tank("t7", 35, level=0),
            Tank("t8", 180, level=180),
        ]
        formula = "25%t1+50%t2+25%t3"
        # Act
        list = tanks.copy()
        remove_useless_tanks(list, formula)

        # Assert
        self.assertEqual(list, [tanks[0],tanks[1], tanks[2],tanks[3], tanks[4], tanks[6]])

    def test_check_tank_formula(self):
        # Arrange
        tank = Tank("t1", 200, 0)
        tank.liquids = [
            Liquid("t1", 50),
            Liquid("t2", 100),
            Liquid("t3", 25),
            Liquid("t4", 25),
        ]
        formula = "25%t1+50%t2+12.5%t3+12.5%t4"

        # Act
        result = check_tank_formula(tank, formula)

        # Assert
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()