# Homework 5

# --- Homework 1 +2 Review ---

# 2.1 Vocabulary Review
"""
1. Git vs. GitHub
Git is different from GitHub because Git is a version control system that allows you to track changes in your code and collaborate with others, while GitHub is a web-based platform that hosts Git repositories

2. Terminal vs. Command Line
The Terminal is an interface with your computer while the Command Line is a way to interact with the Terminal using text commands

3. Local vs. Remote Repository
Local repositories are stored on your device where remote repositories are stored on a server and can be accessed by multiple users

4. Version Control
Version control is a system that allows you to track changes in your code and collaborate with others

5. Staging Area
The staging area is a place where you can prepare your code changes before committing them to the repository

6. git add
git add is used to add changes to the staging area

7. git commit
git commit is used to save changes to the local repository

8. git push
git push is used to upload changes from the local repository to a remote repository

9. git status
git status is used to check the status of your local repository and see which changes have been staged, committed, or are untracked

10. git pull
git pull is used to download changes from a remote repository to the local repository

11. pwd
pwd is a command that prints the current working directory

12. ls
ls is a command that lists the files and directories in the current working directory

13. cd
cd is a command that changes the current working directory to a specified directory

14. nano
nano is a command-line text editor that allows you to create and edit files directly in the terminal

15. touch
touch is a command that creates a new empty file in the current working directory

16. mv
mv is a command that moves or renames files and directories

17. rm
rm is a command that removes files or directories from the current working directory

18. cat
cat is a command that displays the contents of a file in the terminal
"""

# 2.2 A Directory Tree

"""
1. pwd will tell you the current working directory

2. ls will tell you the files and directories in the current working directory

3. cd ../brianna_repo then git pull origin main

4. mv homework.py ../judy_decal/homework

5. cd ../judy_decal/homework

6. cat homework.py

7. git add . then git commit -m "added homework.py" then git push origin main

8. git pull origin main and then git push origin main, she tried to put more stuff in that wasnt in the local repository but was in the remote repository, so she had to pull first before pushing

9. cd ../../../Recent
"""

# --- 3 Homework 3 Review ---

# 3.1 Data Types

def checkDataType(val):
    return type(val).__name__

print(checkDataType(5))  # this will return 'int'

def evenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(evenOrOdd(5))  # this will return 'odd'

# --- 4 Loops ---

numbers = [1, 2, 3, 4, 5]

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sumWithLoop(numbers))  # this will return 15

# --- 5 Homework 4 Review ---

# 5.1 Lists

list = [1, 2, 3, 4, 5]

def duplicateList(list):
    return list + list

print(duplicateList(list))  # this will return [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# 5.2 Debugging

"""
def square(num)
    return num * num

    the above code is missing a colon at the end of the function definition. The correct code should be:
"""

def square(num):
    return num * num

print(square(5))  # this will return 25

# my favorite function was the last one square because I like troubleshooting and debugging the most

print(square(9))  # this will return 81