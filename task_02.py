def coincidence(lis=None, ran=None):
    if lis is None or ran is None:
        return []

    start = ran.start
    stop = ran.stop
    result = []

    for i in lis:
        if isinstance(i, (int, float)) :
            if start <= i < stop:
                result.append(i)
    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))             # => [3, 4, 5]
print(coincidence())                                         # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]
