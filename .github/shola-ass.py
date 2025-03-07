

# 1. ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 2. ValueError
try:
    number = int("not_a_number")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# 3. IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

# 4. KeyError
my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError:
    print("Error: Key not found in the dictionary.")

# 5. TypeError
try:
    result = '1' + 1
except TypeError:
    print("Error: Cannot concatenate string and integer.")

# 6. FileNotFoundError
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")

# 7. AttributeError
class MyClass:
    pass

obj = MyClass()
try:
    obj.some_method()
except AttributeError:
    print("Error: The object has no such method.")

# 8. ImportError
try:
    import non_existent_module
except ImportError:
    print("Error: The module could not be imported.")

# 9. OverflowError
try:
    result = 1.0e+500 * 1.0e+500
except OverflowError:
    print("Error: The result is too large to be represented.")

# 10. AssertionError
try:
    assert 1 + 1 == 3, "Math is broken!"
except AssertionError as e:
    print(f"Error: {e}")
