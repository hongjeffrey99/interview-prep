def flight_itinerary(flights, stack):
	"""Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. All flights must be used in the itinerary.

	For example, given the following list of flights:

	HNL ➔ AKL
	YUL ➔ ORD
	ORD ➔ SFO
	SFO ➔ HNL
	and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL."""
	if not flights:
		return stack
	last_stop = stack[-1]
	for index, (origin, dest) in enumerate(flights):
		other_flights = flights[:index] + flights[index + 1:]
		stack.append(dest)
		if origin == last_stop:
			return flight_itinerary(other_flights, stack)
		stack.pop()
	return None


# test cases

# given case - should return ["YUL", "ORD", "SFO", "HNL", "AKL"]
flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
start = ["YUL"]
print(flight_itinerary(flights, start))

# no such itinerary - should return None
flights = [("HNL", "AKL"), ("YUL", "ORD"), ("SFO", "HNL")]
start = ["YUL"]
print(flight_itinerary(flights, start))

# cycle - should return None, since not all flights can be used
flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL"), ("SFO", "YUL")]
start = ["YUL"]
print(flight_itinerary(flights, start))


