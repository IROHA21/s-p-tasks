def count_words(string):


    result = {}

    if string is None:
        return None
    if not isinstance(string, str):
        return "wrong data type"

    words = string.lower().split()
    for num in words :
        for i in num :
            if i.isalpha() == True :
                pass
        if num in result.keys() :
            result[num] += 1
        else :
            result[num] = 1

    return result





print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo") )# => {"doo": 3, "bee": 2}