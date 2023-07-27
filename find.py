def count_no(n):
    for i in range(n+1):
        c = 0
        x = str(i)
        c = c + x.count('3')

    return c

inp = int(input("Enter a number:"))
result = count_no(inp)
print("result is:", result)