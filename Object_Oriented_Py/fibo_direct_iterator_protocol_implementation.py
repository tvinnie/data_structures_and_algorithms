def fibo(n):
    p = pp = 1
    for n in range(n):
        if n in [0,1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
            
fibs = list(fibo(10))
print(fibs)

# Output
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]