import random

list_one_random = random.randrange(3, 21)
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 17, 18, 19, 20]
list_two = []
print(f'Случайное число: {list_one_random}')
for i in list_one:
    for j in range(i + 1, 21):
        if list_one_random % (i + j) == 0:
            list_two.append(i)
            list_two.append(j)
print(list_two)