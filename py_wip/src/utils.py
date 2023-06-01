import random

from decimal import Decimal as Dec
from typing import Callable, Optional

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

def get_min_tank(tanks: list[Tank]) -> Tank:
    """Returns the tank with the minimum level of the tanks provided."""
    return min(tanks, key=lambda t: t.level)

def get_max_tank(tanks: list[Tank]) -> Tank:
    """Returns the tank with the maximum level of the tanks provided."""
    return max(tanks, key=lambda t: t.level)

def get_largest_tank(tanks: list[Tank]) -> Tank:
    """Returns the tank with the largest capacity available of the tanks provided."""
    return max(tanks, key=lambda t: t.max - t.level)

def get_least_tank(tanks: list[Tank]) -> Tank:
    """Returns the tank with the least capacity available of the tanks provided."""
    return min(tanks, key=lambda t: t.max - t.level)

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

def get_empty_tanks(tanks: list[Tank]) -> list[Tank]:
    """Returns only a list of tanks that are empty."""
    return [tank for tank in tanks if tank.level == 0]

def get_filled_tanks(tanks: list[Tank]) -> list[Tank]:
    return [tank for tank in tanks if tank.level > 0 and tank.level < tank.max]

def get_tanks_in_formula(tanks: list[Tank], parsed_formula: list[tuple[Dec, str]]) -> list[Tank]:
    """Returns only a list of tanks that are in the parsed formula."""
    return [tank for tank in tanks if tank.name in [name for _, name in parsed_formula]]

def aggregate(tanks: list[Tank], parsed_formula: list[tuple[Dec, str]]) -> list[tuple[Dec, Tank]]:
    """Aggregates the parsed formula with the list of tanks provided.

    Parameters
    -------------
    tanks: `list[Tank]`
        The list of tanks to use.
    parsed_formula: `list[tuple[Dec, str]]`
        The formula already parsed, ready to use.

    Returns
    ----------
    `list[tuple[Dec, Tank]]`
        The aggregated list.
    """
    return [
        (
            perc, # %
            [t for t in tanks if t.name == tank_name][0] # tank object
        )
        for perc, tank_name in parsed_formula
    ]

def theoretical_max(tanks: list[Tank], parsed_formula: list[tuple[Dec, str]]) -> Dec:
    """Calculates the maximum theoretical quantity based on the formula and the list of tanks provided.

    Parameters
    -------------
    tanks: `list[Tank]`
        The list of tanks to use.
    formula: `str`
        The formula to use.

    Returns
    -----------
    `Decimal`
        The maximum theoretical quantity.
    """
    zip_tanks = aggregate(tanks, parsed_formula)

    return min([tank.level / (perc / 100) for perc, tank in zip_tanks])

def remove_useless_tanks(tanks: list[Tank], parsed_formula: list[tuple[Dec, str]]) -> None:
    """Removes the tanks that are useless, i.e. the ones that are filled and not in the formula."""
    names = [name for _, name in parsed_formula]
    for tank in tanks.copy():
        if tank.level != 0 and not (tank.name in names):
            tanks.remove(tank)

def get_perc_from_name(name: str, parsed_formula: list[tuple[Dec, str]]) -> Dec:
    """Returns the percentage of the tank in the formula."""
    return Dec([perc for perc, fname in parsed_formula if fname == name][0])

def check_tank_formula(tank: Tank, parsed_formula: list[tuple[Dec, str]], epsilon: Dec = Dec(0.1)) -> Optional[bool]:
    """Checks if each liquids in the tank are in the formula and if their percentage are correct."""
    if not tank.liquids:
        return None

    names = [name for _, name in parsed_formula]

    for liquid in tank.liquids:
        if not liquid.name in names:
            return False

        expected_perc = get_perc_from_name(liquid.name, parsed_formula)
        current_perc = liquid.level * 100 / tank.level
        if abs(current_perc - expected_perc) > epsilon:
            return False

    return True

def generate_percentages(num_percentages: int) -> list[Dec]:
    percentages = []
    remaining_percentage = 100

    for _ in range(num_percentages - 1):
        if remaining_percentage <= 0.1:
            break
        percentage = random.uniform(0.1, remaining_percentage)
        percentage = round(percentage, 4)
        percentages.append(Dec(percentage))
        remaining_percentage -= percentage

    # Calculate the last percentage to ensure the sum is 100%
    percentages.append(Dec(remaining_percentage))

    # Adjust the sum of percentages to ensure it is exactly 100
    diff = 100 - sum(percentages)
    if diff != 0:
        print("call")
        if percentages[-1] + diff > 0:
            percentages[-1] += diff
        else:
            percentages[-2] = percentages[-2]/2
            percentages[-1] = percentages[-2]/2

    return percentages