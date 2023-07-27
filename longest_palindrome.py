def long_pali(string):
    start = 0
    end = len(string) - 1
    while (start <= end):
        if (string[start] == string[end]):
            temp = string[start:end+1]
            check = temp[::-1]
            if (temp == check):
                return temp
            else:
                long_pali(temp)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    long_pali(user_input)
            