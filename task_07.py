def combine_anagrams(list):
    list2 = []
    num = 0
    bib = {}
    list3 = []

    for word in list:
        list2.append(''.join(sorted(word)))
    for word in list2:
        if word not in bib:
            bib[word] = num
            list3.append(num)
            num += 1
        else:
            list3.append(bib[word])

    result = []
    for i in range(num):
        group = []
        for j in range(len(list)):
            if list3[j] == i:
                group.append(list[j])
        result.append(group)

    return result



print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))