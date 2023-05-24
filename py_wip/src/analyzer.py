from typing import Any

class DefaultParser():
    formula: str
    def __init__(self, formula) -> None:
        self.formula = formula

    def decompose(self) -> Any:
        ...

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.formula}/{self.decompose()}"

class FormulaParser(DefaultParser):

    def decompose(self) -> list[tuple[float, str]]:
        output: list[tuple[float, str]] = []
        check_sum = 0
        addends = self.formula.split('+')
        for addend in addends:
            percentage, tank_name = addend.split('%')
            output.append((float(percentage), tank_name))
            check_sum += float(percentage)

        if check_sum != 100.0:
            raise ValueError(f"Sum of percentages is not 100%: {check_sum}%")

        return output

class ListParser(DefaultParser):

    def decompose(self) -> list[tuple[float, float, str]]:
        output = []
        addends = self.formula.split('+')
        for addend in addends:
            capacity, tank_name = addend.split(',')
            currentliq, maxcap = capacity.split('/')
            output.append((float(currentliq), float(maxcap), tank_name))
        return output