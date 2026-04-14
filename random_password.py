import random
def a(l=12):
    lo ="abcdefghijklmnopqrstuvwxyz"
    up ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nu ="0123456789"
    pool = lo+up+nu
    password = "".join(random.choice(pool) for _ in range(l))
    return password
print(a(12))