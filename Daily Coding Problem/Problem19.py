def houses_and_colors(cost):
	"""A builder is looking to build a row of N houses that can be of K different colors. 
	He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

	Given an N by K matrix where the nth row and kth column represents the cost to build the nth house
	with kth color, return the minimum cost which achieves this goal."""

	# Approach: DP
	# Each entry of the solution [i][j] is the minimum cost of painting house i color j, while
	# fulfilling constraints of painting every house <i

	n = len(cost)
	k = len(cost[0])
	solution = [[0] * k]

	"""
	Look at minimum cost of painting each house < i - 1, paint house i - 1 any color except j
		Runs in O(N K ^ 2) time, O(N K) space. Improvement - we only look at the last line, so we can
		keep a single array to only use O(K) space.
	"""
	for r, row in enumerate(cost):
		row_cost = []
		for c, val in enumerate(row):
			row_cost.append(min(solution[r][i] for i in range(k) if i != c) + val)
		solution.append(row_cost)
	return min(solution_matrix[-1])

"""
When looking at total cost of previous row - every time we compute minimum of previous row that isn't
current index. Every element that isn't the index will be the same  alue. When it is the index, it's the
second smallest value. Then we can solely keep track of lowest cost of current row, index of lowest cost,
and second lowest cost.
At value in each row:
1. Check if index is index of lowest cost of previous row. If it is, can't use this color and use the
second lowest cost instead. Otherwise, use lowest cost of prev row
2. Calculate minimum cost if paint this house this particular color
3. Update new lowest cost/index or second lowest cost, depending on which was chosen
"""
from math import inf

def build_houses(matrix):
	lowest_cost, lowest_cost_index = 0, -1
	second_lowest_cost = 0
	for r, row in enumerate(matrix):
	    new_lowest_cost, new_lowest_cost_index = inf, -1
	    new_second_lowest_cost = inf
	    for c, val in enumerate(row):
	        prev_lowest_cost = second_lowest_cost if c == lowest_cost_index else lowest_cost
	        cost = prev_lowest_cost + val
	        if cost < new_lowest_cost:
	            new_second_lowest_cost = new_lowest_cost
	            new_lowest_cost, new_lowest_cost_index = cost, c
	        elif cost < new_second_lowest_cost:
	            new_second_lowest_cost = cost
	    lowest_cost = new_lowest_cost
	    lowest_cost_index = new_lowest_cost_index
	    second_lowest_cost = new_second_lowest_cost

	return lowest_cost

# Tests

# Only one color available with multiple houses - should return None
cost = [[1], [2], [3]]
print(houses_and_colors(cost))

# Regular case - should return 3
cost = [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
print(houses_and_colors(cost))

