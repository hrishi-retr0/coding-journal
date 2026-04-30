#Task: Write a script that takes a string from the user and prints it in reverse.

string = input("Enter the string you would like to reverse: ")

#reversing it using string slicing

reversed_string = string[::-1]

print(f"The reverse of {string} is {reversed_string}")