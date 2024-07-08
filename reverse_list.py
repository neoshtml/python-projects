def reverse_list(list):
    list = [1,2,3,4] 
    reversed_list = []  
    
    for i in range(len(list)):
        reversed_list.append(list[-i-1])

    return reversed_list


output_list = reverse_list([1,2,3,4])
print(output_list)  


def reverse_list(list):
    result=[]
    for i in range(len(list)):
        result.append(list[-i-1])
    print(result)


reverse_list([1,2,3,4])

