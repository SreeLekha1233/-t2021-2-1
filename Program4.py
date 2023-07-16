numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiples = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = {}
for multiple in multiples:
    count = sum(1 for num in numbers if num % multiple == 0)
    result[multiple] = count

print("Output:", result)
