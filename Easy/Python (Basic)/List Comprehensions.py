# Problem: List Comprehensions
# Difficulty: Easy
# Skills: Python (Basic)

# Problem Statement:
# Given four integers x, y, z, and n, generate all possible
# coordinates [i, j, k] of a 3D grid, where:
# 0 <= i <= x, 0 <= j <= y, and 0 <= k <= z.
# Exclude coordinates where i + j + k == n.
# Use a list comprehension and print the resulting list
# in lexicographic increasing order.

# Sample Input:
# 1
# 1
# 1
# 2

# Sample Output:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Explanation:
# Each coordinate component can be either 0 or 1.
# All possible coordinates are generated, but coordinates whose
# components sum to 2 are excluded:
# [0, 1, 1], [1, 0, 1], and [1, 1, 0].
# The remaining coordinates are printed in lexicographic order.

# Solution:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])

# Intuition:
# - Generate every possible combination of i, j, and k within
#   their respective ranges.
# - Keep only the coordinates whose sum is not equal to n.
# - A list comprehension allows us to generate and filter the
#   coordinates in a single expression.

# Explanation:
# - range(x + 1) generates integers from 0 through x.
#   The same logic applies to range(y + 1) and range(z + 1).
# - The three for clauses generate every combination of i, j, and k.
#   The order of the clauses determines the order of the coordinates.
# - [i, j, k] creates a list representing one coordinate.
# - The condition if i + j + k != n excludes coordinates whose
#   components add up to n.
# - The list comprehension collects all remaining coordinates
#   into a list.
# - Because the loops iterate in increasing order, the resulting
#   coordinates are already in lexicographic increasing order.