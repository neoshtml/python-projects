def sum(num):
    result = 0
    for i in range(num):
        current = num - i
        print(current)
        result += current
    return print("Sum:", result)


sum(15)