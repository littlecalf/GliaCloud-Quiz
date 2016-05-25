import math

def nCr(n,r):
    i = math.factorial
    return i(n) // i(r) // i(n - r)

print (nCr(990, 33))