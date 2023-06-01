from src.liquid import Liquid

EPSILON = 0.000000001

class Tank():
    """Represents a tank.

    Attributes
    -------------
    level: `int`
        The level of the tank.
    liquids: List[:class:`TeamMember`]
        The liquids in the tank.
    max: `int`
        The maximum level of the tank.
    name: `str`
        The name of the tank.
    nodes: List[:class:`Tank`]
        The nodes of the tank.
    """

    def __init__(self, name: str, max: float, level: float) -> None:
        if level > max:
            raise ValueError(f"Level > Max in Tank {name}.")

        self.name = name
        self.max = max
        self.nodes = []
        self.liquids = [Liquid(name, level)] if level else []

    @property
    def level(self) -> float:
        return sum([liquid.level for liquid in self.liquids]) if self.liquids else 0

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name}({self.level}/{self.max})"

    def move_unit_to(self, target: "Tank", level: float) -> None:
        """Move a unit of liquid to another tank.
        
        Parameters
        -------------
        target: :class:`Tank`
            The target tank.
        level: `float`
            The level of liquid to move.
        """
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

    def move_perclevel_to(self, target: "Tank", perc: float) -> None:
        """Move a percentage of the current level to another tank.
        
        Parameters
        -------------
        target: :class:`Tank`
            The target tank.
        perc: `float`
            The percentage of the current level to move.
        """
        if target == self:
            return

        if self.level * perc > target.max - target.level :
            if abs(target.max - (self.level * perc)) < EPSILON:
                perc = target.max - self.level / target.max
            else:
                raise ValueError(f"Not enough space available in tank {target} < {perc*100}%  of {self}.")

        if self.level < self.level * perc:
            raise ValueError(f"Not enough liquid available in tank {self} < {perc*100}% of {target}.")

        for liquid in self.liquids:
            target.liquids.append(liquid % perc)