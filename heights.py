data = [{'height': 173, 'first_name': 'John', 'last_name': 'Doe'},
        {'height': 186, 'first_name': 'Tom', 'last_name': 'Hero'},
        {'height': 195, 'first_name': 'John', 'last_name': 'Star'},
        {'height': 165, 'first_name': 'Anna', 'last_name': 'Novok'},
        {'height': 159, 'first_name': 'Anna', 'last_name': 'Novak'},
        {'height': 181, 'first_name': 'Joanna', 'last_name': 'Koval'},
        {'height': 164, 'first_name': 'Joanna', 'last_name': 'Kovol'}]

suma = 0

for record in data:
    suma = suma + record['height']

print(suma)

srednia = suma / len(data)
print(srednia)

data2 = {}

for record in data:
    if record['first_name'] in data2:
        data2[record['first_name']].append(record['height'])
    else:
        data2[record['first_name']] = [record['height']]

print(data2)

for name, heights  in data2.items():
    print(name, sum(heights) / len(heights))

total_by_name = {}
count_by_name = {}

for record in data:
    first_name = record['first_name']
    total_by_name[first_name] = total_by_name.get(first_name, 0) + record['height']
    count_by_name[first_name] = count_by_name.get(first_name, 0) + 1

for name, total in total_by_name.items():
    print(name, total / count_by_name[name])