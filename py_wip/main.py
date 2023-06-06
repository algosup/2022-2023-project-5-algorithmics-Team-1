import random

from src.tank import Tank
from src.utils import check_tank_formula, generate_percentages, get_empty_tanks
from src.solver import Solver

N_TESTS = 15_000
N_START = 1

if __name__ == "__main__":
    stats =  []
    for k in range(N_START, N_TESTS+N_START):
        print(f"Solving randomized N°{k}")
        random.seed(k)

        N_TANKS = random.randint(10, 400)
        MINL_TANK = random.randint(10, 300)
        MAXL_TANK = random.randint(MINL_TANK, 300)

        tanks: list[Tank] = []
        for i in range(1, N_TANKS+1):
            ml = random.randint(MINL_TANK, MAXL_TANK)
            tanks.append(Tank("t"+str(i), ml, flevel=0 if random.choice([0, 1]) == 0 else ml)) # 0 or | FULL

        sorted_tanks = [tank for tank in tanks if tank.level != 0]
        if len(sorted_tanks) < 2:
            print("IMPOSSIBLE")
            continue
        F_TANKS = random.randint(2, len(sorted_tanks))
        FORMULA = ""
        taken_tanks = []
        for perc in generate_percentages(F_TANKS):
            while True:
                selected = random.choice(sorted_tanks)
                if not selected in taken_tanks:
                    taken_tanks.append(selected)
                    FORMULA += str(perc) + "%"+selected.name+"+"
                    break

        solver = Solver(tanks, FORMULA[:-1])

        if solver.max_blend > min(solver.tanks, key=lambda tank: tank.max).max and get_empty_tanks(solver.tanks):
            solver.process_formula(get_empty_tanks(solver.tanks))
        else:
            print("IMPOSSIBLE")
            continue

        success_tanks = [tank for tank in solver.tanks if check_tank_formula(tank, solver.parsed_formula)]
        empt_tanks = get_empty_tanks(solver.tanks)
        waste_tanks = set(solver.tanks) - set(success_tanks) - set(empt_tanks)
        solver.optimize_wasted(empt_tanks, waste_tanks)

        current_success = sum([tank.level for tank in success_tanks])
        current_wasted = solver.waste_tank.level + sum([tank.level for tank in tanks if tank.level != 0 and tank.level != tank.max])
        stats.append((current_success, current_wasted, solver.init_max_blend))

        print("WASTED:", round(current_wasted, 4))  
        print("SUCCESS:", round(current_success, 4), "/", round(solver.init_max_blend, 4), "(theoretical max)", "\n")

    print("STATS:")
    print("Processed:", len(stats))
    print("Mean success:", round(sum([stat[0] for stat in stats]) / len(stats)), '/', round(sum([stat[2] for stat in stats]) / len(stats)))
    print("Mean wasted:", round(sum([stat[1] for stat in stats]) / len(stats)))
    print("Not solved cases:", len([1 for stat in stats if stat[0] == 0]))