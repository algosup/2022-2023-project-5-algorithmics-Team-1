from src.liquid import Liquid

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
    """
    liquids: list[Liquid] = []
    max: float
    name: str = "t0"

    def __init__(self, name: str, max: float, level: float) -> None:
        if level > max:
            raise ValueError(f"Level > Max in Tank {name}.")

        self.name = name
        self.max = max
        self.liquids = [Liquid(name, level)]

    @property
    def level(self) -> float:
        return sum([liquid.level for liquid in self.liquids])

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

        if (target.max - target.level) < level:
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
            raise ValueError(f"Not enough space available in tank {target} < {perc*100}% of {self}.")

        if self.level < self.level * perc:
            raise ValueError(f"Not enough liquid available in tank {self} < {perc*100}% of {target}.")

        for liquid in self.liquids:
            target.liquids.append(liquid % perc)