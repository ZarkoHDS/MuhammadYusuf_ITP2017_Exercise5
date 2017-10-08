#exercise 4
import math
n=int(input("Insert Your Number :"))
def factorial(n):
    try:
        if n ==0:
            return 1
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
    except (RecursionError,TypeError):
        print(None)

print(factorial(n))
