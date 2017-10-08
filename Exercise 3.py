#exercise 3
import math
def hypotenuse(a,b):
    try:
        return math.sqrt(a**2 + b**2)
    except TypeError:
        return None
print(hypotenuse(2,3))
print(hypotenuse("2","3"))
print(hypotenuse(2,"3"))

