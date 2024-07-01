def rev_int(x: int) -> int:
    sign = -1 if x<0 else 1
    x *= sign
    rev = int(str(x)[::-1])
    rev *= sign
    return rev

num = 123
print("Original:", num)
print("Reversed:", rev_int(num))

num = -123
print("Original:", num)
print("Reversed:", rev_int(num))