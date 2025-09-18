from traceback import print_exc


def connect_dicts(dict1, dict2):
    result = {}

    # First determine which dictionary has priority (higher sum)
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    dict1_priority = sum1 > sum2
    print ("priority : ", dict1_priority)
    # Process dict1 keys
    for key1 in dict1.keys():
        if dict1[key1] >= 10:
            # If key exists in both, use the one from priority dict
            if key1 in dict2:
                if dict1_priority:
                    result[key1] = dict1[key1]
                elif dict2[key1] >= 10:
                    result[key1] = dict2[key1]
            else:
                result[key1] = dict1[key1]
    for key2 in dict2.keys():
    # Process dict2 keys for key2 in dict2.keys():
        if dict2[key2] >= 10:
            # Only add if key doesn't exist in result yet (wasn't handled above)
            if key2 not in result:
                result[key2] = dict2[key2]

    # Sort by value
    return dict(sorted(result.items(), key=lambda item: item[1]))


# Test cases
print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => {"d": 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => {"c": 11, "b": 12, "a": 15}