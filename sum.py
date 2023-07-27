x = int(input("Enter a number:"))
while (x!=0):
    sum = 0
    digit = x%10
    sum = x + digit
    x = x//10

print (sum)