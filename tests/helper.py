from decimal import Decimal as Dec

import src.tank as tank

def check_validity(tanks: list[tank.Tank], all: Dec) -> bool:
    return sum([t.level for t in tanks]) == all