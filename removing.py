list = [ 1,4,4,4,4,4,4,6,4,6,4,4,45,78,4,55,4,4,4,4,4,4,8888]

count = 0

for i in list:
    if i == 4:
        count = count + 1

for j in range(count):
    list.remove(4)

print(list)

to_delete = []
for idx, value in enumerate(list):
    if value == 4:
        to_delete.append(idx)
for i in reversed(to_delete):
    del list[i]