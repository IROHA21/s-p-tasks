def max_odd(array):
    max_num = None
    for i in array:
        #check if not float or int
        if not isinstance(i, (int, float)):
            continue

       #convert float to int
        if isinstance(i, float):
            i = int(i)

        #filter based on if odd
        if i % 2 != 0:
            if max_num is None or i > max_num:
                max_num = i

    return max_num



print(max_odd([1, 2, 3, 4, 4]))                  # => 3
print(max_odd([21.0, 2, 3, 4, 4])    )           # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None])) # => 3
print(max_odd(['ololo', 'fufufu']))              # => None
print(max_odd([2, 2, 4]))                        # => None