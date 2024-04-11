# This is a Python script

def my_var():

	var = 42
	print("42 est de type", type(var))
	var = "quarante-deux"
	print("42 est de type", type(var))
	var = "quarante-deux"
	print("quarante-deux est de type", type(var))
	var = 42.0
	print("42.0 est de type", type(var))
	var = True
	print("True est de type", type(var))
	var = [42]
	print("[42] est de type", type(var))
	var = {42: 42}
	print("{42: 42} est de type", type(var))
	var = (42,)
	print("(42,) est de type", type(var))
	var = set()
	print("set() est de type", type(var))


if __name__ == '__main__':
	my_var()