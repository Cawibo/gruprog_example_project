
class Counter:
	""" A very simple counter class that allows for increments and decrements of one (1) and an optional initial value. """
	def __init__(self, initial_value=0):
		self._count = int(initial_value)

	def incr(self):
		self._count += 1

	def decr(self):
		self._count -= 1

	def get_count(self):
		return self._count


if __name__ == "__main__":
	c = Counter()
	assert c.get_count() == 0
	c.incr()
	assert c.get_count() == 1
	c.decr()
	c.decr()
	assert c.get_count() == -1

	c = Counter(10)
	assert c.get_count() == 10