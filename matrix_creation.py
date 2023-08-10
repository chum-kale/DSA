rows = int(input("No of rows:"))
cols = int(input("No of columns:"))

matrix = [[int(input("enter element at {i+1},{j+1}: "))for j in range(cols)]for i in range(rows)]

print ("matrix:")
for row in matrix:
    print(row)