import random

from src.analyzer import FormulaParser
from src.liquid import Liquid
from src.tank import Tank
from src.utils import check_tank_formula, create_nodes, get_empty_tanks, get_largest_tank, get_perc_from_name, get_tanks_with_nodes, print_tanks_nodes, remove_useless_tanks, theoretical_max

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
    print_tanks_nodes(tanks)

    def process(empty_tanks: list[Tank]):
        global max_blend
        try:
            largest_tank = get_largest_tank(empty_tanks)
        except ValueError:
            return
        print(f"Looking for the largest empty tank: {largest_tank.max}")
        if largest_tank.max <= max_blend:
            for tank in get_tanks_with_nodes(tanks):
                tank.move_unit_to(largest_tank, get_perc_from_name(tank.name, PARSED_FORMULA))
                print(f"{tank.name} -> {largest_tank.name} ({get_perc_from_name(tank.name, PARSED_FORMULA)}%)")
            max_blend -= largest_tank.max
            print(f"Champagne left to find space: {max_blend}L")
        else:
            empty_tanks.remove(largest_tank)
            if not empty_tanks:
                print("No more tanks to fill")
                return
            process(empty_tanks)

    print(f"Champagne left to find space: {max_blend}L")
    process(get_empty_tanks(tanks))

    # Check formula for each tank
    print([check_tank_formula(tank, PARSED_FORMULA) for tank in tanks])