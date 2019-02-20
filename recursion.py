import numpy as np


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def Amt(P, r, t):
    if t == 0:
        return P

    else:
        return round(Amt(P * (1 + r), r, t - 1), 2)
