# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")
previous_number = 0

for i in range(1, 11):
    x_sum = previous_number + i
    print("Current number", i, "Previous number", previous_number, "Sum: ", x_sum)
    
    previous_number = i