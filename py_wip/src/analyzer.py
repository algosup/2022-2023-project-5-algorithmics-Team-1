
class FormulaParser():
    formula: str

    def __init__(self, formula: str) -> None:
        self.formula = formula

    def decompose(self) -> list[tuple[float, str]]:
        output: list[tuple[float, str]] = []
        addends = self.formula.split('+')
        for addend in addends:
            percentage, tank_name = addend.split('%')
            output.append((float(percentage), tank_name))
        return output
    

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.formula}/{self.decompose()}"

class ListAnalyzer():
    listanalyzer: str
    def __init__(self , listanalyzer : str) -> None:
        self.listanalyzer = listanalyzer

    def golist(self) -> list[tuple[float, str]]:
        output: list[tuple[float, str]] = []
        addends = self.listanalyzer.split('+')
        for addend in addends:
            capacity, tank_name = addend.split(',')
            currentliq, maxcap = capacity.split('/')
            output.append((str(currentliq),str(maxcap), tank_name))
        return output
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"{self.listanalyzer}/{self.golist()}"

if __name__ == "__main__":
    formula = "50%t1+20%t2+30%t3"
    listanalyzer = "10/100,t1+20/100,t2+30/100,t3"
    parser = FormulaParser(formula)
    analyzer = ListAnalyzer(listanalyzer)
    print(analyzer)
    print(parser)