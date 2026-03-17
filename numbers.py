import random as rnd
import time

while True:
    z = rnd.randint(0,9)
    color = rnd.randint(31,36)

    print(f"\033[{color}m{z}\033[0m", end=" ", flush=True)
    time.sleep(0.051748)
    
