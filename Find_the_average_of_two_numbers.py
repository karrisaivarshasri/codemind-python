numbers = input()
num1, num2 = map(float, numbers.split())

average = (num1 + num2) / 2

average_formatted = "{:.4f}".format(average)

print( average_formatted)
