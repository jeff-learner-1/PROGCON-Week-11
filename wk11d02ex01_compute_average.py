numbers = [0] * (5)

print("Hey there! This program displays the average of the numbers you input.")
print("How many numbers do you need the program to average?")
num = int(input())
total = 0
count = 0
for i in range(0, len(numbers) - 1 + 1, 1):
    print("Input the value of the " + str(i + 1) + " number")
    numbers[i] = int(input())
for i in range(0, len(numbers) - 1 + 1, 1):
    num = numbers[i]
    if num == 0:
        pass
    else:
        total = total + num
        count = count + 1
    if count == 0:
        print(0.0)
    else:
        average = float(total) / count
print(average)

