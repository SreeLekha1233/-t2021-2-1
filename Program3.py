x = int(input("Enter a number (x): "))

numbers = []
for i in range(1, x + 1):
    if i % 2 != 0:
        numbers.append(i)

output = ', '.join(str(num) for num in numbers)
print("Output:", output)
