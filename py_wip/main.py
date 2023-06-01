import random
import sys

from pprint import pprint

from src.analyzer import FormulaParser
from src.liquid import Liquid
from src.tank import Tank
from src.utils import check_tank_formula, create_nodes, generate_percentages, get_empty_tanks, get_filled_tanks, get_largest_tank, get_perc_from_name, get_tanks_with_nodes, remove_useless_tanks, theoretical_max, p_to_n

sys.setrecursionlimit(100_000)

if __name__ == "__main__":
    for i in range(1, 100):
        random.seed(i)
        N_TANKS = random.randint(10, 400)

        MINL_TANK = random.randint(10, 300)
        MAXL_TANK = random.randint(MINL_TANK, 300)

        WASTE_TANK = Tank("waste", 100_000_000, level=0)

        # Create tanks
        tanks: list[Tank] = []
        for i in range(1, N_TANKS+1):
            ml = random.randint(MINL_TANK, MAXL_TANK)
            tanks.append(Tank("t"+str(i), ml, level=0 if random.choice([0, 1]) == 0 else ml)) # 0 or | FULL
            #tanks.append(Tank("t"+str(i), ml, level=random.randint(0, ml))) # 0 to -> FULL 

        sorted_tanks = [tank for tank in tanks if tank.level != 0]
        F_TANKS = random.randint(2, len(sorted_tanks))
        FORMULA = ""
        taken_tanks = []
        gp = generate_percentages(F_TANKS)
        for perc in gp:
            while True:
                selected = random.choice(sorted_tanks)
                if not selected in taken_tanks:
                    taken_tanks.append(selected)
                    FORMULA += str(perc) + "%"+selected.name+"+"
                    break

        PARSED_FORMULA = FormulaParser(FORMULA[:-1]).parse()

        # Get theoretical max based on formula
        max_blend = theoretical_max(tanks, PARSED_FORMULA)
        initial_max = max_blend

        # Remove useless tanks in our list
        remove_useless_tanks(tanks, PARSED_FORMULA)

        # Create nodes for each tank
        create_nodes(tanks)
        
        def next_process(empty_tanks: list[Tank], largest_tank: Tank):
            new_empty = empty_tanks
            new_empty.remove(largest_tank)
            if not new_empty:
                new_empty = get_filled_tanks(tanks)
            process(new_empty)

        def process(empty_tanks: list[Tank]):
            #pprint(tanks)
            global max_blend
            try:
                largest_tank = get_largest_tank(empty_tanks)
            except ValueError:
                #print("EXIT")
                return
            if largest_tank.max <= max_blend:
                if largest_tank.level == 0:
                    #print(f"LARGEST TANK IS EMPTY: {largest_tank}")
                    for tank in get_tanks_with_nodes(tanks):
                        units = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * largest_tank.max
                        #print(f"Moved {units}L from {tank} to {largest_tank}")
                        tank.move_unit_to(largest_tank, units)

                    max_blend -= largest_tank.max

                    next_process(empty_tanks, largest_tank)
                else:
                    for tank in get_tanks_with_nodes(tanks): # get largest tank <= max_blend
                        if tank == largest_tank:
                            units_to_keep = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * tank.max
                            tank.move_unit_to(WASTE_TANK, tank.level - units_to_keep)
                        if largest_tank.max - largest_tank.level <= max_blend:
                            units = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * largest_tank.max  
                            #print(f"Moved {units}L from {tank} to {largest_tank}")
                            tank.move_unit_to(largest_tank, units)
                            
                        # decremente maxblend

                    #print(f"LARGEST TANK IS FULL: {largest_tank}")

            else:
                if max_blend < min(empty_tanks, key=lambda etank: etank.max).max:
                    return
                next_process(empty_tanks, largest_tank)

        #print(f"Champagne left to find space: {max_blend}L")
        # check min max value of each tank
        if max_blend > min(tanks, key=lambda tank: tank.max).max:
            process(get_empty_tanks(tanks))
        else:
            print("IMPOSSIBLE")
            continue

        print("WASTED:", WASTE_TANK.level + sum([tank.level for tank in tanks if tank.level != 0 and tank.level != tank.max]))  
        # print(FORMULA[:-1])
        # for tank in tanks:
        #     if tank.level != 0:
        #         print(tank.name, check_tank_formula(tank, PARSED_FORMULA), tank.liquids)
        print("SUCCESS:", round(sum([tank.level for tank in tanks if check_tank_formula(tank, PARSED_FORMULA)])), "/", initial_max, "(init theoretical max)")
        print()