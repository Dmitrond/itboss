from math import sqrt, pow
import typing as t


def hypotenuse(a: t.Union[int, float], b: t.Union[int, float]) -> float:
    """Returns the hypotenuse"""
    c2 = pow(a, 2) + pow(b, 2)
    c = sqrt(c2)
    return round(c, 2)


print(hypotenuse(3, 4))
print(hypotenuse(3.5, 4.2))
