#! /usr/bin/env python3.6

import time

def Timing(f):
    def Wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print(f"function took {time2 - time1} ms.")
        return ret
    return Wrap

@Timing
def SomeSeldomUsedCal():
    try:
        import numpy as np
    except:
        return -1

    a = np.array(range(10))
    b = np.array(range(10))

    return a+b

@Timing
def Test():
    print("just test");
    return 0


SomeSeldomUsedCal()
SomeSeldomUsedCal()

Test()
