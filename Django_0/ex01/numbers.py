# This is a Python script

def print_numbers():

	try:
		with open("numbers.txt", 'r') as file:
			for line in file:
				numbers = line.strip().split(',')
				for number in numbers:
					print(number)
	
	except FileNotFoundError:
		print("The file doesn't exist.")

if __name__ == '__main__':
	print_numbers()