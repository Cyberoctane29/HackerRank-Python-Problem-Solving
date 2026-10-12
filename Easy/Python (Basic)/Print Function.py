# Problem: Print Function
# Difficulty: Easy
# Skills: Python (Basic)

# Problem Statement:
# Given an integer n, print the integers from 1 through n
# consecutively as a single string, without spaces or line breaks.

# Sample Input:
# 3

# Sample Output:
# 123

# Explanation:
# The integers from 1 through 3 are 1, 2, and 3.
# The end='' argument prevents print() from adding a newline
# after each integer, so the output is 123.

# Solution:
n = int(input())

for i in range(1, n + 1):
    print(i, end='')

# Intuition:
# - Use a for loop to iterate from 1 through n.
# - Print each integer without a separator or newline so that
#   all integers appear consecutively.

# Explanation:
# - int(input()) reads the input and converts it to an integer.
# - range(1, n + 1) generates integers from 1 through n because
#   the stop value of range() is excluded.
# - print(i, end='') prints the current integer and replaces
#   the default newline with an empty string.
# - Repeating this for every integer produces the required output
#   without using any string methods.