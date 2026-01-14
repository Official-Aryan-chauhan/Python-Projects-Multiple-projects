print("Stopwatch")

import time
while True:
    start = input("To Start Time Press s/start : ").lower().strip()
    if start != "" and  start in ("s","start"):
        initial_time  = time.monotonic()
        print("Time Started !")
    else:
        print("Incorrect Value !")
    stop = input("To Stop Press s/stop : ").lower().strip()
    if stop != "" and stop in ( "s","stop"):
        final_time = time.monotonic()
        print("Time Stopped !")
        print(f"Elpsed Time : {round(final_time - initial_time,3)} seconds") 
    else:
        print("Incorrect Value !")
    