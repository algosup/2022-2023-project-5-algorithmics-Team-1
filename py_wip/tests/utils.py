import src.tank as tank

def check_validity(tanks: list[tank.Tank], all: float) -> bool:
    return sum([t.level for t in tanks]) == all

def check_analyzer_validity(result: list[tuple], expectresult: list[tuple]) -> bool:
    return result == expectresult


