import sys

# This is a Python script

def find_capital(w):

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

	w = w.strip()
	if w == "":
		return
	for states_keys, states_values in states.items():
		if states_keys.lower() == w.lower():
			capital = capital_cities[states_values]
			return f"{capital} is the capital of {states_keys}"
	for capital_keys, capital_values in capital_cities.items():
		if capital_values.lower() == w.lower():
			for states_keys, states_values in states.items():
				if capital_keys == states_values:
					return f"{capital_values} is the capital of {states_keys}"
	return f"{w} is neither a capital city nor a state"

def main():

	if len(sys.argv) != 2:
		return
	words = sys.argv[1]
	word = words.split(',')
	for w in word:
		result = find_capital(w)
		if result :
			print(result)

if __name__ == '__main__':
	main()