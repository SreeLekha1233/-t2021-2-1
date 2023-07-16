x = int(input("Enter a number of x: "))

numbers = []
for i in range(1, x + 1):
    numbers.append(2 * i - 1)

output = ', '.join(str(num) for num in numbers)
print("Output:", output)
