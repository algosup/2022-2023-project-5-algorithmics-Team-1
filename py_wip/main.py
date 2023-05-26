import random

from src.analyzer import FormulaParser
from src.liquid import Liquid
from src.tank import Tank
from src.utils import check_tank_formula, create_nodes, get_empty_tanks, get_filled_tanks, get_largest_tank, get_perc_from_name, get_tanks_with_nodes, print_tanks_nodes, remove_useless_tanks, theoretical_max

N_TANKS = 10

MINL_TANK = 100
MAXL_TANK = 300

FORMULA = "25%t2+50%t3+12.5%t4+12.5%t5"
PARSED_FORMULA = FormulaParser(FORMULA).parse()

if __name__ == "__main__":
    random.seed(0)

    random.randint(MINL_TANK, MAXL_TANK)

    # Create tanks
    tanks: list[Tank] = []
    for i in range(1, N_TANKS+1):
        ml = random.randint(MINL_TANK, MAXL_TANK)
        tanks.append(Tank("t"+str(i), ml, level=0 if random.choice([0, 1]) == 0 else ml)) # 0 or | FULL
        #tanks.append(Tank("t"+str(i), ml, level=random.randint(0, ml))) # 0 to -> FULL

    # Get theoretical max based on formula
    max_blend = theoretical_max(tanks, PARSED_FORMULA)

    # Remove useless tanks in our list
    remove_useless_tanks(tanks, PARSED_FORMULA)

    # Create nodes for each tank
    create_nodes(tanks)
    
    def next_process(empty_tanks: list[Tank], largest_tank: Tank):
        new_empty = empty_tanks
        new_empty.remove(largest_tank)
        if not new_empty:
            new_empty = get_filled_tanks(tanks)
            print("EMPTY TANKS", new_empty)
        process(new_empty)

    def process(empty_tanks: list[Tank]):
        print("PROCESSING CALLED")
        global max_blend
        try:
            largest_tank = get_largest_tank(empty_tanks)
        except ValueError:
            print("EXIT")
            return
        if largest_tank.max <= max_blend:
            if largest_tank.level == 0:
                print(f"LARGEST TANK IS EMPTY: {largest_tank}")
                for tank in get_tanks_with_nodes(tanks):
                    units = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * largest_tank.max
                    tank.move_unit_to(largest_tank, units)
                print("LARGEST FILLED",largest_tank)

                max_blend -= largest_tank.max
                print(f"Champagne left to find space: {max_blend}L")
                next_process(empty_tanks, largest_tank)
            else:
                print("LARGEST TANK IS NOT EMPTY")

        else:
            next_process(empty_tanks, largest_tank)


    print(f"Champagne left to find space: {max_blend}L")
    process(get_empty_tanks(tanks))
    
    print(tanks)

    # Check formula for each tank
    print([check_tank_formula(tank, PARSED_FORMULA) for tank in tanks])