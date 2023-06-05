import random

from src.analyzer import FormulaParser
from src.tank import Tank
from src.utils import check_tank_formula, generate_percentages, get_empty_tanks, get_filled_tanks, get_largest_tank, get_perc_from_name, get_tanks_in_formula, remove_useless_tanks, theoretical_max

N_TESTS = 10_000
N_START = 1

if __name__ == "__main__":
    stats =  []
    for k in range(N_START, N_TESTS+N_START):
        random.seed(k)
        N_TANKS = random.randint(10, 400)

        MINL_TANK = random.randint(10, 300)
        MAXL_TANK = random.randint(MINL_TANK, 300)

        WASTE_TANK = Tank("waste", 100_000_000, flevel=0)

        # Create tanks
        tanks: list[Tank] = []
        for i in range(1, N_TANKS+1):
            ml = random.randint(MINL_TANK, MAXL_TANK)
            tanks.append(Tank("t"+str(i), ml, flevel=0 if random.choice([0, 1]) == 0 else ml)) # 0 or | FULL
            #tanks.append(Tank("t"+str(i), ml, flevel=random.randint(0, ml))) # 0 to -> FULL 

        sorted_tanks = [tank for tank in tanks if tank.level != 0]
        if len(sorted_tanks) < 2:
            print("IMPOSSIBLE")
            continue
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
        
        print(f"Solving randomized N°{k}")

        max_blend = theoretical_max(tanks, PARSED_FORMULA)
        initial_max = max_blend
        steps = []

        remove_useless_tanks(tanks, PARSED_FORMULA)

        def next_process(empty_tanks: list[Tank], largest_tank: Tank):
            new_empty = empty_tanks
            new_empty.remove(largest_tank)
            if not new_empty:
                new_empty = get_filled_tanks(tanks)
            process(new_empty)

        def process(empty_tanks: list[Tank]):
            global max_blend
            largest_tank = get_largest_tank(empty_tanks)
            if largest_tank.max <= max_blend:
                if largest_tank.level == 0:
                    for tank in get_tanks_in_formula(tanks, PARSED_FORMULA):
                        units = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * largest_tank.max
                        tank.move_unit_to(largest_tank, units)
                        print(f"{tank.name} {round(units, 4)}L -> {largest_tank.name}")

                    max_blend -= largest_tank.max

                    next_process(empty_tanks, largest_tank)
                else:
                    for tank in get_tanks_in_formula(tanks, PARSED_FORMULA): # get largest tank <= max_blend
                        if tank == largest_tank:
                            units_to_keep = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * tank.max
                            tank.move_unit_to(WASTE_TANK, tank.level - units_to_keep)
                            print(f"{tank.name} {round(tank.level - units_to_keep, 4)}L -> {WASTE_TANK.name}")
                        if largest_tank.max - largest_tank.level <= max_blend:
                            units = get_perc_from_name(tank.name, PARSED_FORMULA) / 100 * largest_tank.max  
                            tank.move_unit_to(largest_tank, units)
                            print(f"{tank.name} {round(units, 4)}L -> {largest_tank.name}")
                    max_blend -= largest_tank.max - largest_tank.level

            else:
                if max_blend < min(empty_tanks, key=lambda etank: etank.max).max:
                    return
                next_process(empty_tanks, largest_tank)

        if max_blend > min(tanks, key=lambda tank: tank.max).max and get_empty_tanks(tanks):
            process(get_empty_tanks(tanks))
        else:
            print("IMPOSSIBLE")
            continue

        success_tanks = [tank for tank in tanks if check_tank_formula(tank, PARSED_FORMULA)]
        empt_tanks = get_empty_tanks(tanks)
        waste_tanks = set(tanks) - set(success_tanks) - set(empt_tanks)

        def optimize_wasted(empty_tanks: list[Tank], wasted_tanks: list[Tank]):
            if len(empty_tanks) == 0 or len(wasted_tanks) == 0:
                return
            largest_empty = get_largest_tank(empty_tanks)
            max_waste = max(wasted_tanks, key=lambda tank: tank.level)
            if largest_empty.max < max_waste.level:
                max_waste.move_unit_to(largest_empty, largest_empty.max)
                print(f"{max_waste.name} {round(largest_empty.max, 4)}L -> {largest_empty.name}")
                wasted_tanks.remove(max_waste)
                empty_tanks.remove(largest_empty)
                optimize_wasted(empty_tanks, wasted_tanks)
            else:
                empty_tanks.remove(largest_empty)
                optimize_wasted(empty_tanks, wasted_tanks)

        print("OPTIMIZING WASTED TANKS")
        optimize_wasted(empt_tanks, waste_tanks)

        current_success = sum([tank.level for tank in tanks if check_tank_formula(tank, PARSED_FORMULA)])
        current_wasted = WASTE_TANK.level + sum([tank.level for tank in tanks if tank.level != 0 and tank.level != tank.max])
        stats.append((current_success, current_wasted, initial_max))

        print("WASTED:", current_wasted)  
        print("SUCCESS:", current_success, "/", initial_max, "(init theoretical max)", "\n")

    print("STATS:")
    print("Processed:", len(stats))
    print("Mean success:", round(sum([stat[0] for stat in stats]) / len(stats)), '/', round(sum([stat[2] for stat in stats]) / len(stats)))
    print("Mean wasted:", round(sum([stat[1] for stat in stats]) / len(stats)))
    print("Not solved cases:", len([stat for stat in stats if stat[0] == 0]))