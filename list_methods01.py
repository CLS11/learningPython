#removing duplicates from the list
numbers = [5, 5, 5, 1, 2, 9, 3, 2, 1]
numbers2 = []
for num in numbers:
    if num not in numbers2:
        numbers2.append(num)
print(numbers2)
