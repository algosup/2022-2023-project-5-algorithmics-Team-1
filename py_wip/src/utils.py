from typing import Callable

from src.analyzer import FormulaParser
from src.tank import Tank

def _percentage_to_number(perc: float, total: float) -> float:
    return (perc / 100) * total
p_to_n: Callable = _percentage_to_number
"""Convert a percentage to a number based on the total.

Parameters
-------------
perc: `float`
    The percentage to convert.
number: `float`
    The number to convert.

Returns
----------
`float`
    The converted number.
"""

def _number_to_percentage(number: float, total: float) -> float:
    return (number / total) * 100
n_to_p: Callable = _number_to_percentage
"""Convert a number to a percentage based on the total.

Parameters
-------------
number: `float`
    The number to convert.
total: `float`
    The total to convert.

Returns
----------
`float`
    The converted percentage.
"""

def get_min_level(tanks: list[Tank]) -> float:
    """Returns the minimum level of the tanks provided."""
    return min([t.level for t in tanks])

def get_name_from_tanks(tanks: list[Tank]) -> str:
    """Returns the shortneid name of the tanks provided."""
    return ",".join([t.name[1:] for t in tanks])

def create_nodes(tanks: list[Tank]) -> None:
    """Creates the nodes for each tank based on the other tanks."""
    for tank in tanks:
        tank.nodes = [
            other
            for other in tanks
            if tank != other
            and tank.level > 0
            and other.max - other.level >= tank.level
            and other not in tank.nodes
        ]

def print_tanks_nodes(tanks: list[Tank]) -> None:
    """A debug method that prints each tanks with their shortnied nodes name."""
    for tank in tanks:
        print(f"{tank} -> {get_name_from_tanks(tank.nodes)}")

def get_tanks_with_nodes(tanks: list[Tank]) -> list[Tank]:
    """Returns only a list of tanks that have nodes."""
    return [tank for tank in tanks if len(tank.nodes) > 0]

def aggregate(tanks: list[Tank], parsed_formula: list[tuple[float, str]]) -> list[tuple[float, Tank]]:
    """Aggregates the parsed formula with the list of tanks provided.

    Parameters
    -------------
    tanks: `list[Tank]`
        The list of tanks to use.
    parsed_formula: `list[tuple[float, str]]`
        The formula already parsed, ready to use.

    Returns
    ----------
    `list[tuple[float, Tank]]`
        The aggregated list.
    """
    return [
        (
            perc, # %
            [t for t in tanks if t.name == tank_name][0] # tank object
        )
        for perc, tank_name in parsed_formula
    ]

def theoretical_max(tanks: list[Tank], formula: str) -> float:
    """Calculates the maximum theoretical quantity based on the formula and the list of tanks provided.

    Parameters
    -------------
    tanks: `list[Tank]`
        The list of tanks to use.
    formula: `str`
        The formula to use.

    Returns
    -----------
    `float`
        The maximum theoretical quantity.
    """
    parsed_formula = FormulaParser(formula).decompose()

    zip_tanks = aggregate(tanks, parsed_formula)

    return min([tank.level / (perc / 100) for perc, tank in zip_tanks])

def remove_useless_tanks(tanks: list[Tank], formula: str) -> None:
    """Removes the tanks that are useless, i.e. the ones that are filled and not in the formula."""
    names = [name for _, name in FormulaParser(formula).decompose()]
    for tank in tanks.copy():
        if tank.level != 0 and not (tank.name in names):
            tanks.remove(tank)

def check_tank_formula(tank: Tank, formula: str, epsilon: float = 0.1) -> bool:
    parsed_formula = FormulaParser(formula).decompose()
    names = [name for _, name in parsed_formula]

    for liquid in tank.liquids:
        if not liquid.name in names:
            raise ValueError(f"Error in tank: {tank}, contains liquid {liquid}")

        index = names.index(liquid.name)
        expected_perc = parsed_formula[index][0]
        current_perc = tank.level * liquid.level / 100
        if abs(current_perc - expected_perc) > epsilon:
            raise ValueError(f"Error in tank: {tank}, liquid {liquid} | curr:{current_perc} != exp:{expected_perc}")

    return True