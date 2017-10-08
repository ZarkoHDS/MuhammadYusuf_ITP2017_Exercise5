#exercise 9
def my_gen(n):
    z = n
    while z >= 0:
        yield z
        z -= 1
for x in my_gen(10):
    print(x,end=" ")
