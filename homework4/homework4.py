# homework4.py

# --- 3 Lists ---

# 3.1 List Operators

fav_foods = ["sushi", "pizza", "corndogs", "ice cream", "tacos"]

print(fav_foods[1]) # prints the second item in the list

print(fav_foods[-1]) # prints the last item in the list

fav_foods.append("chocolate") # adds "chocolate" to the end of the list
print(fav_foods[-1])

fav_foods.insert(0, "ramen") # adds "ramen" to the beginning of the list
print(fav_foods[0])

del fav_foods[2] # removes the third item in the list
print(fav_foods)

print(len(fav_foods)) # prints the length of the list

for food in fav_foods: # prints each item in fav_foods in upper case 
    print(food.upper())

new_fav_foods = fav_foods[:: len(fav_foods) -1] # creates a new list with the first and last items in fav_foods
print(new_fav_foods) 

if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!") # prints "No potato!" because "potato" is not in fav_foods

# 3.2 Slicing and Striding

numbers = list(range(0, 21)) # creates a list of numbers from 0 to 20

def get_first_15(numbers): # returns the first 15 numbers in the list
    return numbers[:15]

def get_every_5th(numbers): # returns every 5th number in the list
    return numbers[::5]

def reverse_and_stride(numbers): # returns the list in reverse order and returns every 3rd number
    return numbers[::-3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print("original list:", numbers)
print("first 15 numbers:", step1)
print("every 5th number:", step2)
print("reverse and stride:", step3)

# 3.3 Nested Lists

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2][0:3]) # prints the third row of the nested list

print(numbers[1][1]) # prints the second item in the second row of the nested list

numbers.append([10, 11, 12]) # adds a new row to the nested list
print(numbers)

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for num in row:
            total += num
    return total

print(sum_nested(numbers)) # prints the sum of all numbers in the nested list

# 3.4 Create a 5x5 List

def create_5x5_list():
    grid = []
    number = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(number)
            number += 1
        grid.append(row)
    return grid

initial_list = create_5x5_list()
print(initial_list)

def mult_of_3(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] % 3 == 0:
                grid[i][j] = "?"
    return grid

modified_list = mult_of_3(initial_list)
print(modified_list)

def sum_of_remaining():
    total = 0
    for row in modified_list:
        for num in row:
            if num != "?":
                total += num
    return total

total_sum_result = sum_of_remaining()
print(total_sum_result) 

# --- 4 Dictionaries ---

# 4.1 Dictionary Operations

ages = {
    "Katie": 30,
    "Miriam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"]) # prints Katie's age

ages["Mira"] = 100 # changes Mira's age to 100
print(ages["Mira"])

ages["Milana"] = 52 # adds Milana to the dictionary
print(ages)

del ages["Miriam"] # removes Miriam from the dictionary
print(ages)

for name, age in ages.items(): # prints each name and age in the dictionary
    print(f"{name}: {age}")

# my favorite function is the sum_nested(numbers) fucntion
print(sum_nested(numbers))