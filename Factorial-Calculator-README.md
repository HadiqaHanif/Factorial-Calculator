# Factorial Calculator 🔢

A simple Python program that calculates the **factorial** of a number entered by the user, with proper handling for negative numbers and zero.

## 📌 What It Does
Factorial of a number `n` (written as `n!`) is the product of all positive integers from `1` to `n`.
Example: `5! = 5 × 4 × 3 × 2 × 1 = 120`

This script:
- Takes user input
- Handles **negative numbers** (invalid case) separately
- Handles **zero** (`0! = 1`) correctly
- Calculates factorial for **positive numbers** using a loop

## 🖥️ Code
```python
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("Factorial is: 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial is:", factorial)
```

## ▶️ How to Run
```bash
python factorial.py
```

## 💡 Example Outputs
```
Enter a number: 5
Factorial is: 120

Enter a number: 0
Factorial is: 1

Enter a number: -3
Factorial is not defined for negative numbers.
```

## 🛠️ Requirements
- Python 3.x (no external libraries needed)

## 🚀 Possible Improvements
- Add error handling for non-numeric input
- Implement a recursive version
- Compare with Python's built-in `math.factorial()`

## 🏷️ Topics
`python` `factorial` `beginner-project` `math` `loops`
