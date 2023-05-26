import unittest

from src.analyzer import FormulaParser
from src.liquid import Liquid
from src.tank import Tank
from src.utils import *

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
        parsed_formula = FormulaParser(formula).parse()

        # Act
        maximum = theoretical_max(tanks, parsed_formula)

        # Assert
        self.assertEqual(maximum, 150)

    def test_number_to_percentage(self):
        # Arrange
        number = 90
        total = 180

        # Act
        percentage = n_to_p(number, total)

        # Assert
        self.assertEqual(percentage, 50)

    def test_percentage_to_number(self):
        # Arrange
        percentage = 50
        total = 180

        # Act
        number = p_to_n(percentage, total)

        # Assert
        self.assertEqual(number, 90)

    def test_get_min_tank(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=80),
        ]
        
        # Act
        minimum = get_min_tank(tanks)
        minimum_level = minimum.max

        # Assert
        self.assertEqual(minimum_level, 25)

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
        parsed_formula = FormulaParser(formula).parse()

        # Act
        list = tanks.copy()
        remove_useless_tanks(list, parsed_formula)

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
        parsed_formula = FormulaParser(formula).parse()

        # Act
        result = check_tank_formula(tank, parsed_formula)

        # Assert
        self.assertEqual(result, True)


    def test_get_empty_tanks(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=0),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 80, level=0),
        ]

        # Act
        empty_tanks = get_empty_tanks(tanks)

        # Assert
        self.assertEqual(empty_tanks, [tanks[0], tanks[3]])

    def test_get_max_tank(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 200, level=200),
            Tank("t4", 80, level=80),
        ]

        # Act
        max_tank = get_max_tank(tanks)

        # Assert
        self.assertEqual(max_tank, tanks[2])

    def test_get_largest_tank(self):
        # Arrange
        tanks = [
            Tank("t1", 100, level=100),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 150, level=150),
        ]

        # Act
        largest_tank = get_largest_tank(tanks)

        # Assert
        self.assertEqual(largest_tank, tanks[3])


    def test_get_least_tank(self):
        # Arrange
        tanks = [
            Tank("t1", 10, level=10),
            Tank("t2", 75, level=75),
            Tank("t3", 25, level=25),
            Tank("t4", 150, level=150),
        ]

        # Act
        least_tank = get_least_tank(tanks)

        # Assert
        self.assertEqual(least_tank, tanks[0])



if __name__ == "__main__":
    unittest.main()