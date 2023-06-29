age = 3

# ternary operator
is_baby = 'baby' if age < 2 else 'not a baby'

# print(is_baby)

# TRY / EXCEPT 

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")

# divide(10, 2)

# DICTIONARY MAPPING
# if/elif/else statements are typically the preferred method 

dog = 'hungry'

dict_map = {
    'hungry': 'Refilling food bowl.',
    'thirsty': 'Refilling water bowl.',
    'playful': 'Playing tug-of-war.',
    'cuddly': 'Snuggling.'
}

owner = dict_map.get(dog, "Reading newspaper.")
# Remember that a dictionary's .get() method lets us set a default value! In this case it doesn't look like it does anything lol.

print(owner)