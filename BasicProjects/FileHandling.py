def extract_title(file):
	file_open = open(file)
	output = []
	x = ''
	contents = file_open.read()
	a = ''
	final = contents.split()
	for char in final:
		if char == 'TITLE':
			x = 'TITLE'
			continue
		if char == 'JOURNAL':
			break
		if x == 'TITLE':
			output.append(char + ' ')
			continue

	a = a.join(output)
	a = a.strip(' ')
	return a
	file_open.close()

def extract_organism(file):
	file_open = open(file)
	output = []
	x = ''
	a = 0
	for char in file_open:
		if x != '':
			break
		if 'ORGANISM' in char:
			for char in file_open:
				if 'REFERENCE' not in char:
					hold = char.strip('/n')
					x = x + str(hold)
					continue
				break
					
	x = ' '.join(x.split())
	
	x = x.split(';')
	
	for i in x:
		if a >= 0:
			y = i.strip()
			y = y.strip('.')
		output.append(y)
	return output

def extract_sequences(name):
	dict = {}
	z = 0
	file_open = open(name)
	for i in file_open:
		if 'ORIGIN' in i:
			for i in file_open:
				if '//' not in i:
					y = i.strip('/n')
					a, b = y.split(None, 1)
					dict[int(int(a))] = b.split()
					continue
				break
	return dict
	file_open.close()