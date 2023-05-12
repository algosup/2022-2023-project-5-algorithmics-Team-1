class Tank():
    level: float
    max: float
    name: str = "t0"

    def __init__(self, name: str, max: float, level: float = -1) -> None:
        if level > max:
            raise ValueError(f"Level > Max in Tank {name}.")

        self.name = name
        self.max = max
        self.level = self.max if level == -1 else level

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.name}({self.level}/{self.max})"

    def move_to(self, target: "Tank", level: float) -> None:
        if target == self:
            return

        if (target.max - target.level) < level:
            raise ValueError(f"Free in Tank {target} < {level}.")

        if self.level < level:
            raise ValueError(f"Level in Tank {self} < {level}.")

        self.level -= level
        target.level += level