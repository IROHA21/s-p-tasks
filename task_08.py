def multiply_numbers(variable=None):
    count = 1
    if variable is None:
        return None
    elif not isinstance(variable, str):
        variable = str(variable)

    has_digits = False
    for elem in variable:
        if elem.isdigit():
            count = count * int(elem)
            has_digits = True

    if has_digits:
        return count
    else:
        return None




print(multiply_numbers())          # => None
print(multiply_numbers('ss'))      # => None
print(multiply_numbers('1234'))    # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3))      # => 6
print(multiply_numbers([5, 6, 4])) # => 120