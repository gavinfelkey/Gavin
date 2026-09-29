# homework3.py

# --- 3 Print Functions ---

def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye("Gavin") # says goodbye

def circle_area(radius):
    return((radius ** 2) * 3.14)

print(circle_area(4)) # prints teh area of a circle

# --- 4 Return Functions ---

# in class we covered adding
def add( a, b):
    return a + b

def subtract( a, b):
    return a - b

def multiply( a, b):
    return a * b

def divide( a, b):
    return a / b

print(add( 6, 8)) # adds
print(subtract( 8, 3)) # subtracts
print(multiply( 3, 5)) # multiplies
print(divide( 9, 3)) # divides

# --- 5 Conditionals ---

readings = [15, 14, 17, 20, 23, 28, 20]

def what_to_wear(readings): #displays the low and high temps of the readings list
    low = min(readings)
    high = max(readings)
    return(low, high)

print(what_to_wear(readings))

def is_weekend(day): # in class we did this one
    if day == "Saturday" or day == "Sunday":
        return "Its the Weekend!"
    else:
        return "Its not the weekend :("

print(is_weekend("Monday"))

days = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sudnay": 7}
def weekdays(days):
    if days == 1 or days == 2 or days == 3 or days ==4 or days == 5:
        return True
    else:
        return False

print(weekdays(6)) # uses dictionary to take an integer to tell whether is weekday or not returning true or false accordingly

def fuel_efficiency(miles, gallons):
    return(divide(miles, gallons))

print(fuel_efficiency(12, 5)) #used previously defined divide function we did earlier in section 4

def encryption(number):
    last_digit = number % 10
    remaining_digits = number // 10
    multiplier = 10 ** len(str(remaining_digits))
    return((last_digit * multiplier) + remaining_digits)

print(encryption(58348487)) #moves last digit to front 

# --- 6 Loops ---

def power_function(x, y):
    starting = 1
    for num in range(y):
        starting *= x
    return starting

print(power_function(2, 6)) # does ** but without the use of that shortcut

# for loops

integers = [5, 37, 1, 3, 43,20]

def minimum(integers):
    min_int = integers[0]
    for int in integers:
        if int < min_int:
            min_int = int
    return min_int

print(minimum(integers)) #finds minimum of a list without the use of the min function

def maximum(integers):
    max_int = integers[0]
    for int in integers:
        if int > max_int:
            max_int = int
    return max_int

print(maximum(integers)) #finds the maximum of a lsit without the use of the max function

# while loops

def find_min(integers):
    min_int = integers[0]
    i = 1
    while i < len(integers):
        if integers[i] < min_int:
            min_int = integers[i]
        i += 1
    return min_int

print(find_min(integers)) #finds minimum of a list without the use of the min function using a while loop

def find_max(integers):
    max_int = integers[0]
    i = 1
    while i < len(integers):
        if integers[i] > max_int:
            max_int = integers[i]
        i += 1
    return max_int

print(find_max(integers)) #finds maximum of a list without the use of the min function using a while loop

def sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num = num // 10
    return digit_sum 

print(sum(85743)) # adds digits of number in function

# --- 7 Running Your Script ---

num = 42342
result = sum(num) # addition of digits in num
print(f"the result of calculate the sum (6.3) with num = {num} is {result}")