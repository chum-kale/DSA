def repeat(string):
    string.replace(" ", "")
    char_array = list(string)
    temp = []
    for i in len(char_array):
        if (char_array[i] == char_array[i+1]):
            x = char_array[i]
        y = char_array.count(x)
        temp.append(y)

    return max(temp)