import random

from src.tank import Tank
from src.utils import create_nodes, print_tanks_nodes, remove_useless_tanks, theoretical_max

N_TANKS = 10

MINL_TANK = 100
MAXL_TANK = 300

FORMULA = "25%t1+50%t2+12.5%t3+12.5%t4"

if __name__ == "__main__":
    random.seed(0)

    random.randint(MINL_TANK, MAXL_TANK)

    # Create tanks
    tanks: list[Tank] = []
    for i in range(1, N_TANKS+1):
        ml = random.randint(MINL_TANK, MAXL_TANK)
        #tanks.append(Tank('t'+str(i), ml, level=0 if i % 2 == 0 else ml)) # 0 or | FULL
        tanks.append(Tank('t'+str(i), ml, level=random.randint(0, ml))) # 0 to -> FULL

    # Get theoretical max based on formula
    max_blend = theoretical_max(tanks, FORMULA)

    # Remove useless tanks in our list
    remove_useless_tanks(tanks, FORMULA)

    # Create nodes for each tank
    create_nodes(tanks)

    #? Print tanks and their nodes (DEBUG)
    print_tanks_nodes(tanks)

def wip_test():
    # Check different possible mixes between tanks
    for i in range(1, N_TANKS+1):
        for j in range(i+1, N_TANKS+1):
            print(f'Check mix between {tanks[i-1]} and {tanks[j-1]}')