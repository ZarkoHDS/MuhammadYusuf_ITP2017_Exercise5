#exercise 8

z = lambda a:a**2
x = lambda a,b:(a**2 + b**2)
c = lambda *args:sum(args)/len(args)
v = lambda k:"".join(set(k))

def z(a):
    return a**2
def x(a,b):
    return (a**2 + b**2)
def c(*args):
    return sum(args)/len(args)
def v(k):
    return "".join(set(k))
