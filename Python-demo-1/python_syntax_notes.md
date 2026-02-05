# Python Fundamentals: Syntax Overview

These notes cover the core building blocks of Python. Python is designed to be readable and uses **indentation** (spaces) to define blocks of code.

---

## 1. Variables and Data Types
Variables store information. You don't need to declare their type (like `int` or `string`); Python figures it out for you.

```python
name = "Justin"         # String (text)
age = 20                # Integer (whole number)
score = 95.5            # Float (decimal)
is_student = True       # Boolean (True/False)

# Printing variables
print(f"Hello {name}, you are {age} years old.")
```

---

## 2. Basic Math
Python uses standard math symbols.

```python
total = 10 + 5    # Addition
diff = 10 - 5     # Subtraction
prod = 10 * 5     # Multiplication
quot = 10 / 5     # Division (always returns a float)
power = 10 ** 2   # Exponent (10 squared)
```

---

## 3. If Statements (Control Flow)
Used to make decisions. Use `if`, `elif`, and `else`.

```python
if age >= 21:
    print("You can enter!")
elif age >= 18:
    print("You can enter, but no drinks.")
else:
    print("Too young!")
```

---

## 4. Lists (Collections)
Lists stores multiple items in a single variable. They are **zero-indexed** (start counting at 0).

```python
fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])      # Prints "Apple"
fruits.append("Pear") # Adds to the end
fruits[1] = "Mango"   # Changes "Banana" to "Mango"
print(len(fruits))    # Prints how many items are in the list
```

---

## 5. Loops (Doing things repeatedly)

### For Loops
Great for iterating over a list or a range of numbers.

```python
# Loop through a list
for fruit in fruits:
    print(f"I like {fruit}")

# Loop a specific number of times
for i in range(5):
    print(f"Count: {i}") # Prints 0, 1, 2, 3, 4
```

### While Loops
Runs as long as a condition is true.

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")
```

---

## 6. Functions
Functions are reusable blocks of code.

```python
def greet(user_name):
    return f"Hello, {user_name}!"

message = greet("Alice")
print(message)
```

---

## 7. Helpful Tips
- **Indentation**: Python relies on 4 spaces (or a tab) to know what code belongs inside an `if` statement or a loop.
- **Comments**: Use `#` to write notes in your code that Python will ignore.
- **Errors**: Don't be afraid of them! They usually tell you exactly which line is broken.
