class Liquid():
    name: str
    level: float

    def __init__(self, name: str, level: float) -> None:
        self.name = name
        self.level = level

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Liq[{self.name}:{self.level}]"

    def __mod__(self, perc: float) -> "Liquid":
        source_level = self.level
        self.level = self.level - (source_level * perc)
        return Liquid(self.name, source_level * perc)

    def __truediv__(self, num: float) -> "Liquid":
        source_level = self.level
        self.level /= num
        return Liquid(self.name, source_level - self.level)