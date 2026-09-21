
# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number combining both an integer and a fractional component

c = 3j
print(3j)
print(type(3j)) # c is a complex, a complex number containing both a real and imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of text characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, an ordered collection of values

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, an undordered collection of key-value pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an unordered and unchangable colection of elements

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list of strings, a mutable sequence holding text data

i = True
print(i)
print(type(i)) # i is a boolean, a truth value which is only ever true or false

j = None
print(j)
print(type(j)) # j is a NoneType, an absence of value or a null value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list of mixed data types

l = str(14)
print(l)
print(type(l)) # l is a string, the text before the integer changes it into a string

m = 1e4
print(m)
print(type(m)) # m is a float, all exponentials are always made as a float

n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, an unordered and mutable collection of unique elements

"""
1. I found a total of 9 different data types
2. string, integer, float, complex, list, dictionary, tuple, boolean, and nonetype
3. b and m are floats, d and l are strings, and e, h ,k are all lists
4. The data type of l is a string, this is because of the str() which chnanges the given data type into a string, so although it was an integer it was changed by the function prior to it
5. varable n above
"""

# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9

print(10 == 9) # False, 10 is not equal to 9

print(10 <= 9) # False, 10 is not less than or equal to 9

print(bool("abc")) # True, non-empty strings are true

print(bool(123)) # True, non-zero numbers are true

print(bool(["apple", "cherry", "banana"])) # True, non-empty lists are true

print(bool(True)) # True, the boolean value True is true

print(bool(False)) # False, the boolean value False is false

print(bool(0)) # False, the integer 0 is false

print(bool("")) # False, empty strings are false

print(bool(" ")) # True, non-empty strings are true even if they contain only whitespace

print(bool(())) # False, empty tuples are false

print(bool([])) # False, empty lists are false

print(bool({})) # False, empty sets are false

print(bool(True and False)) # False, True and False evaluates to False

print(bool(True and True)) # True, True and True evaluates to True

print(bool(False and False)) # False, False and False evaluates to False

print(bool(True or False)) # True, True or False evaluates to True

print(bool(True or True)) # True, True or True evaluates to True

print(bool(False or False)) # False, False or False evaluates to False

print(bool(not(False))) # True, not(False) evaluates to True

print(bool(not(True))) # False, not(True) evaluates to False

"""
1. If there is information inside of the bool funtion it will return true, if not then it will give false, in teh latter it is false if it can be and true otherwise.
2. The most shocking result is the one with bool("") and booll(" ") because teh first one is false and the seond is true although the only difference is that the second one has a space.
3. bool(not(False) or not(False)), this is true because not(False) is true so the statement evaluates to bool(True or True) which we know is True
4. bool(not(True) and not(True)), this is false because not(True) is false so the statement evaluates to bool(False and False) which we know is False
"""

# --- Operators ---

# Arithmetic Operators

print(10 + 5) # 15, addition

print(10 - 5) # 5, subtraction

print(2 * 4) # 8, multiplication

print(6 / 3) # 2.0, division

print(5 % 2) # 1, modulus, returns the remainder of the division

print(3 ** 2) # 9, exponentiation, raises the number to the power of the second number

print(15 // 2) # 7, floor division, returns the largest integer less than or equal to the division result

# Comparison Operators

print(5 == 2) # False, checks if 5 is equal to 2

print(10 != 10) # False, checks if 10 is not equal to 10

print(2 < 5) # True, checks if 2 is less than 5

print(12 > 5) # True, checks if 12 is greater than 5

print(5 <= 6) # True, checks if 5 is less than or equal to 6

print(1 >= 10) # False, checks if 1 is greater than or equal to 10

# Assignment Operators

x=5
print(x)

x += 5 # 10, adds 5 to x and assigns the result back to x
print(x)

x -= 4 # 6, subtracts 4 from x and assigns the result back to x
print(x)

x *= 3 # 18, multiplies x by 3 and assigns the result back to x
print(x)

# Logical Operators

"""
the and operator returns True if both parts are True, otherwise it returns False
print(bool(True and True)) = True
print(bool(True and False)) = False

the or operator returns True if at least one part is True, otherwise it returns False
print(bool(True or False)) = True
print(bool(False or False)) = False

the not operator returns the opposite boolean value of the part it is applied to
print(bool(not(False))) = True
print(bool(not(True))) = False
"""

# More Questions

"""
the difference between / and // is that / returns a float value while // returns an integer value
the difference between % and // is that % returns the remainder of the division while // returns the largest integer less than or equal to the division result
I would use the % to calculate the remainder when dividing two numbers, print(10 % 3) would return 1
Assignment operators work by taking the current value of a variable and performing an operation on it, then assigning the result back to the variable
"""

# --- Strings ---

my_string = "hello"
print(my_string) # Prints: hello

print(my_string[0]) # Prints: h, the first character of the string

print(my_string[1]) # Prints: e, the second character of the string

print(my_string[2]) # Prints: l, the third character of the string

print(my_string[3]) # prints l, the fourth character of the string

print(my_string[4]) # prints o, the fifth character of the string

print(my_string[-1]) # prints o, the last character of the string

print(my_string[1:3]) # prints el, the characters from index 1 to 2 (3 is not included)

print(my_string[0:5:2]) # prints hlo, the characters from 0 to 5 while skipping every second character

print(len(my_string)) # prints 5, the length of the string

print(my_string + "goodbye") # prints hellogoodbye, concatenation of two strings

print(7 * my_string) # prints hellohellohellohellohellohellohello, repetition of the string 7 times

# Questions

# 1. Slicing is the process of extracting a portion of a string by specifying a range of indices. The manipulations with which I sliced my string were my_string[1:3] which returned el and my_string[0:5:2] which returned hlo.
name = "Oski"
print("Hello, my name is", name)
# 2. it printed Hello, my name is Oski, this is because the print command listed everything in the order it was given and separated by a space, so it printed the string first and then the variable name second.
name = "Oski"
print(f"Hello, my name is {name}")
# 3. it printed Hello, my name is Oski, ignoring the f in front the name variable assigned to teh same Oski was slipped into the string given with the brackets around it
# 4. The main difference between the two methods is that the first method uses concatenation to combine strings and variables, while the second method uses f-strings to embed variables directly into the string.

# Teminal Commands

"""
1. cd
changes directories. use it to move from one folder to another
Example: cd Desktop
2. ls
lists the contents of the current directory. use it to see what files and folders are in the current directory
Example: ls
3. ls -a
lists all files and directories, including hidden ones. use it to see all files and folders in the current directory, including those that are hidden
Example: ls -a
4. mkdir
creates a new directory. use it to create a new folder in the current directory
Example: mkdir new_folder
5. cat
displays the contents of a file. use it to view the contents of a text file in the terminal 
Example: cat file.txt
6. pwd
prints the current working directory. use it to see the full path of the current directory
Example: pwd
7. cd ..
moves up one directory level. use it to go back to the parent directory of the current directory
Example: cd ..
8. cd .
changes directory to the current folder. use it to stay in the current directory
Example: cd .
9. cd ~
changes directory to the home folder. use it to go to the home directory of the current user
Example: cd ~
10. cp
copies a file or directory. use it to make a copy of a file or folder
Example: cp file.txt copy_of_file.txt
11. mv
moves a file or directory. use it to move a file or folder to a different location
Example: mv file.txt new_folder/
12. rm
removes a file or directory. use it to delete a file or folder
Example: rm file.txt
13. clear
clears the terminal screen. use it to remove all previous commands and output from the terminal window
Example: clear
14. grep
searches for a specific pattern in a file or output. use it to find specific text within files or command output
Example: grep "search_term" file.txt
15. touch
creates a new empty file. use it to create a new text file in the current directory
Example: touch new_file.txt
16. echo
prints text to the terminal. use it to display a message or the value of a variable
Example: echo "Hello, World!"
17. man
displays the manual for a command. use it to learn more about a specific command and its options
Example: man ls
18. ls -l
lists the contents of a directory in long format, showing additional details such as file permissions ownership and size
Example: ls -l
19. rm -r
removes a directory and its contents recursively. use it to delete a folder and all of its files and subfolders
Example: rm -r folder_name
20. mkdir -p
creates a directory and any necessary parent directories. use it to create nested folders in one command
Example: mkdir -p parent_folder/child_folder
"""

# Questions

"""
1. touch, echo, man
2. ls lists all contents in a file, while ls -a lists all contents including hidden files
3. a hidden file is a file that is not normally visible when listing the contents of a directory. an example is . or ..
4. ls -l, rm -r, mkdir -p
"""