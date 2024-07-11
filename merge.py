def merge_list():
    list1 = [1, 2, 7, 11]
    list2 = [3, 4, 6, 9]

    merged_list = []
    i, l = 0, 0

    while i < len(list1) and l < len(list2):
        if list1[i] < list2[l]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[l])
            l += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while l < len(list2):
        merged_list.append(list2[l])
        l += 1

    return merged_list

print(merge_list())