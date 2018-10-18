def lecture_rooms(intervals):
	# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
	# find the minimum number of rooms required.
	# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

	start = sorted(start for start, end in intervals)
	end = sorted(end for start, end in intervals)

	current_overlap = 0
	current_max = 0
	i = 0 
	j = 0
	while i < len(intervals) and j < len(intervals):
		if start[i] < end[j]:
			print(current_overlap)
			current_overlap += 1
			current_max = max(current_max, current_overlap)
			i += 1
		else:
			current_overlap -= 1
			j += 1
	return current_max

# Tests
# Given, should return 2
intervals = [(30, 75), (0, 50), (60, 150)]
print(lecture_rooms(intervals))

# All overlapping, should return 2
# intervals = [(30, 75), (25, 35), (60, 100)]
print(lecture_rooms(intervals))

# No overlapping, should return 1
intervals = [(10, 20), (30, 40), (40, 50)]
print(lecture_rooms(intervals))