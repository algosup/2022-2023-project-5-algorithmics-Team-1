import unittest

from src.analyzer import ListParser, FormulaParser

class TestAnalyzer(unittest.TestCase):

    def test_listparser(self):
        # Arrange
        listanalyzer = "10.45/100,t1+20/100.55,t2+30.11111/100.0987654321,t3"
        expected = [(10.45, 100.0, "t1"), (20.0, 100.55, "t2"), (30.11111, 100.0987654321, "t3")]

        # Act
        analyzer = ListParser(listanalyzer)
        result = analyzer.decompose()

        # Assert
        self.assertEqual(result, expected)


    def test_formulaparser(self):
        # Arrange
        formula = "50.2%t1+19.8%t2+30.0%t3"
        expected = [(50.2, "t1"), (19.8, "t2"), (30.0, "t3")]
        # Act
        parser = FormulaParser(formula)
        result = parser.decompose()
        # Assert
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()