import src.tank as tank

def check_validity(tanks: list[tank.Tank], all: float) -> bool:
    return sum([t.level for t in tanks]) == all