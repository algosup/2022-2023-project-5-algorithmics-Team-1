from src.analyzer import FormulaParser
from src.tank import Tank
from src.utils import get_filled_tanks, get_largest_tank, get_perc_from_name, get_tanks_in_formula, remove_useless_tanks, theoretical_max

class Solver():
    def __init__(self, tanks: list[Tank], formula: str):
        self.parsed_formula = FormulaParser(formula).parse()
        remove_useless_tanks(tanks, self.parsed_formula)
        self.tanks = tanks
        self.tanks_formula = get_tanks_in_formula(tanks, self.parsed_formula)
        self.max_blend = theoretical_max(tanks, self.parsed_formula)
        self.init_max_blend = self.max_blend
        self.steps = []

        self.waste_tank = Tank("waste", 100_000_000, 0)

    def to_next_process(self, empty_tanks: list[Tank], largest_tank: Tank):
        empty_tanks.remove(largest_tank)
        if not empty_tanks:
            empty_tanks = get_filled_tanks(self.tanks)
        self.process_formula(empty_tanks)

    def process_formula(self, empty_tanks: list[Tank]):
        largest_tank = get_largest_tank(empty_tanks)
        if largest_tank.max <= self.max_blend:
            if largest_tank.level == 0:
                for tank in self.tanks_formula:
                    units = get_perc_from_name(tank.name, self.parsed_formula) / 100 * largest_tank.max
                    tank.move_unit_to(largest_tank, units)
                    self.steps.append((tank.name, round(units, 4), largest_tank.name))
                self.max_blend -= largest_tank.max
                self.to_next_process(empty_tanks, largest_tank)
            else:
                for tank in self.tanks_formula: # get largest tank <= max_blend
                    if tank == largest_tank:
                        units_to_keep = get_perc_from_name(tank.name, self.parsed_formula) / 100 * tank.max
                        tank.move_unit_to(self.waste_tank, tank.level - units_to_keep)
                        self.steps.append((tank.name, round(tank.level - units_to_keep, 4), self.waste_tank.name))
                    if largest_tank.max - largest_tank.level <= self.max_blend:
                        units = get_perc_from_name(tank.name, self.parsed_formula) / 100 * largest_tank.max  
                        tank.move_unit_to(largest_tank, units)
                        self.steps.append((tank.name, round(units, 4), largest_tank.name))
                self.max_blend -= largest_tank.max - largest_tank.level
        else:
            if self.max_blend < min(empty_tanks, key=lambda etank: etank.max).max:
                return
            self.to_next_process(empty_tanks, largest_tank)

    def optimize_wasted(self, empty_tanks: list[Tank], wasted_tanks: list[Tank]):
        if len(empty_tanks) == 0 or len(wasted_tanks) == 0:
                return
        largest_empty = get_largest_tank(empty_tanks)
        max_waste = max(wasted_tanks, key=lambda tank: tank.level)
        empty_tanks.remove(largest_empty)
        if largest_empty.max < max_waste.level:
            max_waste.move_unit_to(largest_empty, largest_empty.max)
            self.steps.append((max_waste.name, round(largest_empty.max, 4), largest_empty.name))
            wasted_tanks.remove(max_waste)
            self.optimize_wasted(empty_tanks, wasted_tanks)
        else:
            self.optimize_wasted(empty_tanks, wasted_tanks)