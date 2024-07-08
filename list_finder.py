def list_finder(num):
    list=[3,8,19,21,42]
    if num in list:
        return True
    else:
        return False


print(list_finder(19))

def list_finder(num):
    list=[3,8,19,21,42]
    result=False
    for item in list:
        if(num==item):
            result=True
    print(result)


list_finder(19)