import sys

# This is a Python script

def find_capital():

	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	for states_keys, states_values in states.items():
		if sys.argv[1] == states_keys:
			for capital_keys, capital_values in capital_cities.items():
				if states_values == capital_keys:
					print(capital_values)
					return
	print("toto")

def main():

	if len(sys.argv) != 2:
		return
	find_capital()

if __name__ == '__main__':
	main()