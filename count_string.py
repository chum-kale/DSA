x = int(input("Enter a number:"))
string = str(x)
for i in range(len(string)):
    count = 0
    if (string[i] == '3'):
        count =count+1

print (count)