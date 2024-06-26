# This is a Python script

def get_musicians():

	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	return d

def make_dict(musicians_list):
    return {year: name for name, year in musicians_list}

def display_dict(musicians_dict):
    for key, value in musicians_dict.items():
        print(f'{key} : {value}')

if __name__ == '__main__':
	display_dict(make_dict(get_musicians()))