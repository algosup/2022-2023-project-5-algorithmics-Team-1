from decimal import Decimal as Dec
from typing import Union

class Liquid():
    def __init__(self, name: str, flevel: Union[float, Dec]) -> None:
        self.name = name
        self.level = Dec(flevel)

    def __truediv__(self, fnum: Union[float, Dec]) -> "Liquid":
        num = Dec(fnum)
        source_level = self.level
        self.level /= num
        return Liquid(self.name, source_level - self.level)

    def __mod__(self, fperc: Union[float, Dec]) -> "Liquid":
        perc = Dec(fperc)
        source_level = self.level
        self.level = self.level - (source_level * perc)
        return Liquid(self.name, source_level * perc)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Liq[{self.name}:{self.level}]"