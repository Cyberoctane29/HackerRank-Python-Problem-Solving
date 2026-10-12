
# Problem: Python: Division
# Difficulty: Easy
# Skills: Problem Solving (Basic)

# Problem Statement:
# Given two integers, a and b, print two lines:
# 1. The integer division result (a // b).
# 2. The float division result (a / b).

# Sample Input:
# 4
# 3

# Sample Output:
# 1
# 1.3333333333333333

# Explanation:
# - 4 // 3 = 1 because integer division rounds down to the
#   nearest integer.
# - 4 / 3 = 1.3333333333333333 because regular division
#   returns a floating-point result.

# Solution:
a = int(input())
b = int(input())

print(a // b)
print(a / b)

# Intuition:
# - Python provides two division operators: // for floor division
#   and / for regular division.
# - Apply each operator to the same pair of integers and print
#   the results separately.

# Explanation:
# - int(input()) reads each input line and converts it to an integer.
# - a // b performs floor division, returning the greatest integer
#   less than or equal to the quotient.
# - a / b performs regular division and returns a floating-point result.
# - Each print() call displays its result on a separate line.
