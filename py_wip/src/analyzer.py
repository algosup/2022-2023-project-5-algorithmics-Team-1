from decimal import Decimal as Dec
from typing import Any

class DefaultParser():
    formula: str
    def __init__(self, formula) -> None:
        self.formula = formula

    def parse(self) -> Any:
        ...

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.formula}/{self.parse()}"

class FormulaParser(DefaultParser):

    def parse(self) -> list[tuple[Dec, str]]:
        output: list[tuple[Dec, str]] = []
        check_sum = 0
        addends = self.formula.split('+')
        for addend in addends:
            percentage, tank_name = addend.split('%')
            output.append((Dec(round(float(percentage), 4)), tank_name))
            check_sum += Dec(percentage)

        if round(check_sum) != Dec(100):
            raise ValueError(f"Sum of percentages is not 100%: {check_sum}%")

        return output

class ListParser(DefaultParser):

    def parse(self) -> list[tuple[Dec, Dec, str]]:
        output = []
        addends = self.formula.split('+')
        for addend in addends:
            capacity, tank_name = addend.split(',')
            currentliq, maxcap = capacity.split('/')
            output.append((Dec(currentliq), Dec(maxcap), tank_name))
        return output