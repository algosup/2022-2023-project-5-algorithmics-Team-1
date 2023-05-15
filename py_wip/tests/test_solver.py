import unittest

from .utils import check_validity
from src.solver import Solver
from src.tank import Tank

class TestSolver(unittest.TestCase):

    def test_solver(self):
        # Arrange
        tanks: list[Tank] = [Tank('t'+str(i), 100, level=i*10) for i in range(1, 10)]
        # Act
        solver = Solver()
        solver.method(tanks)
        # Assert
        self.assertIs(check_validity(tanks, 450), True)