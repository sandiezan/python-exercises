#Write a Python code to accept a string from the user and display characters present at an even index number.

original_string = input("What's your favourite word? ")
print("The original string is", input)

string_length = len(original_string)

print("Printing only even index characters")
x = list(original_string)
for i in x[0::2]:
    print(i)