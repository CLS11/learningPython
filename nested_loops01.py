#numbers = [5, 2, 5, 2, 2] -> F
numbers = [2, 2, 2, 2, 5] #L
for num in numbers:
    output = ''
    for count in range(num):
        output += 'x'
    print(output)
