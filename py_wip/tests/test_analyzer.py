import unittest

from .utils import check_validity
from src.analyzer import ListAnalyzer, FormulaParser

class TestAnalyzer(unittest.TestCase):

    def test_analyzer(self):
        # Arrange
        listanalyzer = "10/100,t1+20/100,t2+30/100,t3"
        exceptresult = [('10', '100', 't1'), ('20', '100', 't2'), ('30', '100', 't3')]
        # Act
        analyzer = ListAnalyzer(listanalyzer)
        result = analyzer.golist()
        # Assert
        self.assertEqual(check_validity(result, exceptresult), True)


    def test_formula(self):
        # Arrange
        formula = "50%t1+20%t2+30%t3"
        exceptresult = [(50.0, 't1'), (20.0, 't2'), (30.0, 't3')]
        # Act
        parser = FormulaParser(formula)
        result = parser.decompose()
        # Assert
        self.assertEqual(check_validity(result, exceptresult), True)
