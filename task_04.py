def sort_list(list):


    if not list :
        return []

    minimum = min(list)
    maximum = max(list)


    for i in range(len(list)) :

        if list[i] == minimum :
            list[i] = maximum
        elif list[i] == maximum:
            list[i] = minimum
           



    list.append(minimum)
    return list



print(sort_list([]))           # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1]))          # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]