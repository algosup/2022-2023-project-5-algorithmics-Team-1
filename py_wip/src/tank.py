from decimal import Decimal as Dec
from typing import Union

from src.liquid import Liquid

EPSILON = 0.0000000001

class Tank():
    """Represents a tank.

    Attributes
    -------------
    level: `Decimal`
        The level of the tank.
    liquids: List[:class:`TeamMember`]
        The liquids in the tank.
    max: `Decimal`
        The maximum level of the tank.
    name: `str`
        The name of the tank.
    nodes: List[:class:`Tank`]
        The nodes of the tank.
    """

    def __init__(self, name: str, fmax: float, flevel: float) -> None:
        if flevel > fmax:
            raise ValueError(f"Level > Max in Tank {name}.")

        max, level = Dec(fmax), Dec(flevel)

        self.name = name
        self.max = max
        self.nodes = []
        self.liquids = [Liquid(name, level)] if level else []

    @property
    def level(self) -> Dec:
        return Dec(sum([liquid.level for liquid in self.liquids])) if self.liquids else Dec(0)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name}({self.level}/{self.max})"

    def move_unit_to(self, target: "Tank", flevel: Union[float, Dec]) -> None:
        """Move a unit of liquid to another tank.
        
        Parameters
        -------------
        target: :class:`Tank`
            The target tank.
        flevel: `Union[float, Decimal]`
            The level of liquid to move.
        """
        level = Dec(flevel)
        if level < 0:
            raise ValueError(f"Cannot move negative amount of liquid {level}.")
        if (target.max - target.level) < level:
            if abs(target.max - target.level - level) < EPSILON:
                level = target.max - target.level
            else:
                raise ValueError(f"Not enough space available in tank {target} < {level}.")

        if self.level < level:
            raise ValueError(f"Not enough liquid available in tank {self} < {level}.")
        self.move_perclevel_to(target, level / self.level)

    def move_perclevel_to(self, target: "Tank", fperc: Union[float, Dec]) -> None:
        """Move a percentage of the current level to another tank.
        
        Parameters
        -------------
        target: :class:`Tank`
            The target tank.
        fperc: `Union[float, Decimal]`
            The percentage of the current level to move.
        """
        if target == self:
            return

        perc = Dec(fperc)

        if self.level * perc > target.max - target.level :
            if abs(target.max - target.level - (self.level * perc)) < EPSILON:
                perc = (self.level * perc) / self.level
            else:
                raise ValueError(f"Not enough space available in tank {target} < {perc*100}% ({self.level * perc}) of {self}.")

        if self.level < self.level * perc:
            raise ValueError(f"Not enough liquid available in tank {self} < {perc*100}% of {target}.")

        for liquid in self.liquids:
            target.liquids.append(liquid % perc)