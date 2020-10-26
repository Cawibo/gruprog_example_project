
from counter import Counter

def main():
	counter = None

	while True:
		while counter is None:
			print("There is no counter available, do you want to create one?")
			if (resp := input("y/n: ")) == "y":
				print("Creating counter...")
				counter = Counter(input("Initial value: "))
			elif resp == "n":
				print("ok... <.<")
			else:
				print("only accepts 'y' or 'n'")

		print("Counter is currently at: " + str(counter.get_count()))
		
		if (resp := input("'incr'|'decr'|'new'|'quit'? ")) == "incr":
			counter.incr()
		elif resp == "decr":
			counter.decr()
		elif resp == "new":
			counter = None
		elif resp == "quit":
			print("Exiting...")
			break
		else:
			print("'{}' is not a valid input.".format(resp))

if __name__ == "__main__":
	main()