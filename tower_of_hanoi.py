def toh(n, r1, r2, r3):
    if n == 0:
        return
    toh(n-1, r1, r2, r3)
    print("Move disk", n, "from rod", r1, "to rod", r2)
    toh(n-1, r2, r3, r1)

N = 3
toh(N, "A", "B", "C")