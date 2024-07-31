def sumoflist(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
sample_list = [8, 2, 3, 0, 7]
total = sumoflist(sample_list)
print(f"The sum of the list is: {total}")
