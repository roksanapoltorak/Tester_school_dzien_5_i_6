dict1 = {'bar': 'foo', 'spam': 'eggs', 'baz': 'foo', 'ban': 'foo', 'fried': 'eggs'}

dict2 = {}

for key, value in dict1.items():
    if value not in dict2:
        dict2[value] = [key]
    else:
        dict2[value].append(key)