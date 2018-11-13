list1 = ['A', 'b', 'hello', 1, 2]

print(list1)
print(list1[-4])
print(list1[1:4])

new_list = list1[:3]
print(new_list)
print(new_list[1])

blank_list = []
for i in range(10):
    blank_list.append(i)
print(blank_list)

second_list = [i for i in range(10)]
print(second_list)