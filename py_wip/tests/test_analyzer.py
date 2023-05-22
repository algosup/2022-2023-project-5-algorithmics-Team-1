import unittest

from .utils import check_analyzer_validity
from src.analyzer import ListAnalyzer, FormulaParser
from src.tank import Tank

class TestAnalyzer(unittest.TestCase):

    def test_analyzer(self):
        # Arrange
        listanalyzer = "10/100,t1+20/100,t2+30/100,t3"
        expectresult = [('10', '100', 't1'), ('20', '100', 't2'), ('30', '100', 't3')]
        # Act
        analyzer = ListAnalyzer(listanalyzer)
        result = analyzer.golist()
        # Assert
        self.assertTrue(check_analyzer_validity(result, expectresult), True)


    def test_formula(self):
        # Arrange
        formula = "50%t1+20%t2+30%t3"
        expectresult = [(50.0, 't1'), (20.0, 't2'), (30.0, 't3')]
        # Act
        parser = FormulaParser(formula)
        result = parser.decompose()
        # Assert
        self.assertTrue(check_analyzer_validity(result, expectresult), True)

if __name__ == "__main__":
    unittest.main()
