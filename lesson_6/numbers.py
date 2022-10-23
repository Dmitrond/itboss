numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.append(10)

numbers[1] = numbers[1] * 2
numbers[3] = numbers[3] * 2
numbers[5] = numbers[5] * 2
numbers[7] = numbers[7] * 2
numbers[9] = numbers[9] * 2

numbers[2] = numbers[2] * 3
numbers[5] = numbers[5] * 3
numbers[8] = numbers[8] * 3

numbers[3] = numbers[3] * 4
numbers[7] = numbers[7] * 4

if numbers[0] < 3:
    numbers[0] = numbers[0] * 5

if numbers[3] >= 7:
    numbers[3] = numbers[3] / 4

print(sum(numbers))










