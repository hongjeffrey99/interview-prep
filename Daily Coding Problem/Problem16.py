"""
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
		i is guaranteed to be smaller than or equal to N.
"""

class Log(object):
	def __init__(self, n):
		self.n = n
		self._log = []
		self._cur = 0

	def record(self, order_id):
		if len(self.log) == self.n:
			self._log[self._cur] = order_id
		else:
			self._log.append(order_id)
		self._cur = (self._cur + 1) % self.n

	def get_last(self, i):
		return self._log[self._cur - i]

"""
This structure is called a ring buffer. Uses index wrapping to avoid having to shift
elements of array on pop, which is O(N).
This implementation is thus better because record and get_last now have constant time
"""