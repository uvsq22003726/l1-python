def f(a,x):
    a += 1
    x[0] = 45
a = 0
b = [13]
f(a,b)
print(a,b)