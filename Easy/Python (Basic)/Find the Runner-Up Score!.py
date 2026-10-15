# Problem: Find the Runner-Up Score!
# Difficulty: Easy
# Skills: Python (Basic)

# Problem Statement:
# Given n scores, store them in a list and find the runner-up score.
# The runner-up is the second-highest distinct score.

# Sample Input:
# 5
# 2 3 6 6 5

# Sample Output:
# 5

# Explanation:
# The given scores are [2, 3, 6, 6, 5].
# The highest score is 6.
# The second-highest distinct score is 5.
# Therefore, the runner-up score is 5.


# Solution 1:
n = int(input())
arr = list(map(int, input().split()))

print(sorted(set(arr))[-2])

# Intuition:
# - Remove duplicate scores, sort the remaining scores in ascending
#   order, and select the second-last element.

# Explanation:
# - map(int, input().split()) converts the space-separated scores
#   into integers.
# - list() stores those integers in a list.
# - set(arr) removes duplicate scores, so the highest score appears
#   only once.
# - sorted(set(arr)) returns the distinct scores in ascending order.
# - [-2] accesses the second-last element, which is the second-highest
#   distinct score.


# Solution 2:
n = int(input())
arr = map(int, input().split())
arr = list(arr)

m = max(arr)
arr1 = [x for x in arr if x < m]

print(max(arr1))

# Intuition:
# - Find the highest score, exclude every occurrence of that score,
#   and then find the maximum among the remaining scores.

# Explanation:
# - map(int, input().split()) converts the input scores into integers.
# - list(arr) materializes the map object into a list so it can be
#   used multiple times.
# - max(arr) finds the highest score and stores it in m.
# - The list comprehension [x for x in arr if x < m] keeps only
#   scores strictly below the highest score.
# - max(arr1) returns the highest score among those remaining scores,
#   which is the runner-up.


# Solution 3:
n = int(input())
arr = list(map(int, input().split()))

print(max(x for x in arr if x < max(arr)))

# Intuition:
# - Find the maximum score and use a generator expression to consider
#   only scores below it. Then find the maximum of those scores.

# Explanation:
# - list(map(int, input().split())) creates a list of integer scores.
# - max(arr) finds the highest score.
# - The generator expression (x for x in arr if x < max(arr))
#   yields only scores strictly below the highest score.
# - max() finds the largest value among those yielded scores.
# - This produces the second-highest distinct score without explicitly
#   creating another list.
# - Note: max(arr) is recalculated for each item examined by the
#   generator expression, so Solution 2 avoids this repeated work
#   by calculating the maximum only once.