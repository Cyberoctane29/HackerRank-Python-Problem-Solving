
# Problem: Arithmetic Operators
# Difficulty: Easy
# Skills: Python, Arithmetic Operators, Input/Output

# Problem Statement:
# Given two integers, a and b, print three lines:
# 1. Their sum (a + b).
# 2. Their difference (a - b).
# 3. Their product (a * b).

# Sample Input:
# 3
# 2

# Sample Output:
# 5
# 1
# 6

# Explanation:
# 3 + 2 = 5
# 3 - 2 = 1
# 3 * 2 = 6

# Solution:
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

# Intuition:
# - Read the two integers and apply the three arithmetic operations
#   in the order specified by the problem.

# Explanation:
# - int(input()) reads a line of input and converts it to an integer.
# - a + b adds the two integers.
# - a - b subtracts the second integer from the first.
# - a * b multiplies the two integers.
# - Each print() call outputs its result on a separate line.
