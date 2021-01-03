#defines the how_odd function
def how_odd(n):
#declares variable x equal to 0
	x = 0
#if there is no remainder, execute
	if n % 2 == 0:
		return x
#if there is remainder, execute
	while n % 2 != 0:
#n is divded by 2
		n = int(n/2)
#x increased by 1 according to pattern
		x += 1
#if no remainder, execute
		if n % 2 == 0:
			return x

#defines the vibrate(n) function
def vibrate(n):
#declares x is equal to 0
	x = 0
#if true, execute
	if n == 1:
		return x
#if not true, execute
	elif n != 1:
#creates while loop that follows even number protocol
		while n % 2 == 0:
			if n == 1:
				return x
			n = int(n * 4/3) + 1
			x += 1
#creates while loop that follows odd number protocol
			while n % 2 != 0:
				if n == 1:
					return x
				n = int(n / 3)
				x += 1
#if resulting number is even, break out of loop and go back to even
				while n % 2 == 0:
					break
#creates while loop that follows odd number protocol
		while n % 2 != 0:
			if n == 1:
				return x
			n = int(n / 3)
			x += 1
##creates while loop that follows even number protocol
			while n % 2 == 0:
				if n == 1:
					return x
				n = int(n * 4/3) + 1
				x += 1	
#if resulting number is even, break out of loop and go back to even
				while n % 2 == 0:
					break
				break

#creates the is_combustible function
def is_combustible(name, combustibles):
#iterates x over combustibles
	for x in combustibles:
#if the name is combustible, return it
		if name == x:
			return True
#else return false
	return False

#creates the biggest_combustible function
def biggest_combustible(names, sizes, combustibles):
#if combustible list empty, return none 
	if len(combustibles) == 0:
		return None
#if names list empty, return none 
	if len(names) == 0:
		return None
#two variables to be used in the future
	largest_combust_val = 0
	i = 0
#iterates x over range of names
	for x in range(len(names)):
#if names is combustible, execute
		if names[x] in combustibles:
#starting value for i
			i = sizes[x]
#if i is larger then current largest combustible variable, replace it
			if i > largest_combust_val:
				largest_combust_val = i
#if the function is on its last name, return the largest_combust_val
			if x == len(names) - 1:
				return names[sizes.index(largest_combust_val)]
#if the function is on its last name, return the largest_combust_val
		elif largest_combust_val > 0 and x == len(names) - 1:
			return names[sizes.index(largest_combust_val)]
#if no combustible names, return none
		elif x == len(names) - 1:
			return None
		
#creates the any_oversized function
def any_oversized(sizes, maximum):
#iterates x over the sizes
	for x in sizes:
#if x is bigger than the maxmimum val, return True
		if x > maximum:
			return True
#else return false
	return False

#creates the any_adjacent_combustibles function	
def any_adjacent_combustibles(names, combustibles):
#declares variable i to be used later
	i = 0
#if names list is empty, return false
	if len(names) == 0:
		return False
#iterates x over range of names
	for x in range(len(names)):
#if the name is combustible, execute
		if names[x] in combustibles:
#one iteration passed
			i += 1
#two iterations in a row mean theyre next to eachother
			if i >= 2:
				return True
#if we are on the last name and none next to eachother, return false
			elif x == len(names) - 1:
				return False
#else continue the function
			else:    
				continue
#if we are on the last name and none next to eachother, return false
		elif x == len(names) - 1:
			return False
#none next eachother, set i equal back to 0
		else:
			i = 0

#creates the get_combustibles function			
def get_combustibles(names, combustibles):
#creates two variables to be used later
	list = []
	y = 0
#if names list empty, return none
	if len(names) == 0:
		return None
#if combustibles list empty, return none
	if len(combustibles) == 0:
		return None
#iterates x over names
	for x in names:
#passes one iteration of y
		y += 1
#if found in combustible, execute
		if x in combustibles:
			list += [x]
#if end of function is reached, return list
		if y == len(names):
			return list
			
#creates the cheap_products function
def cheap_products(names, prices, limit):
#creates two variables to be used later
	list = []
	y = 0
#if names list empty, return none
	if len(names) == 0:
		return list
#if prices list empty, return none
	if len(prices) == 0:
		return list
#iterates x over the range of names
	for x in range(len(names)):
#sets the cost of the name
		cost = prices[x]
#if cost is equal/under the limit, put it in the list
		if cost <= limit:
			list += names[x]
#if the last name is reached, return existing list
		if x == len(names) - 1:
			return list

#creates the box_sort function
def box_sort(names, sizes):
#creates a list that will hold all the boxes
	list = [[], [], [], []]
#as item is iterated over range of names
	for item in range(len(names)):
#sets how large the item is
		fit = sizes[item]
#if the item can fit in box, execute and add to list
		if fit <= 2:
			list[0] += [names[item]]
			if item == len(names) - 1:
				return list
			continue
#if the item can fit in box, execute and add to list
		elif fit <= 5:
			list[1] += [names[item]]
			if item == len(names) - 1:
				return list
			continue
#if the item can fit in box, execute and add to list
		elif fit <= 25:
			list[2] += [names[item]]
			if item == len(names) - 1:
				return list
			continue
#if the item can fit in box, execute and add to list
		elif fit <= 50:
			list[3] += [names[item]]
			if item == len(names) - 1:
				return list
			continue
#if the last name is reached, return existing list
		elif item == len(names) - 1:
			return list
#if name doesnt fix in any boxes, continue
		elif fit > 50 or fit < 0:
			continue

#creates the packing_list function
def packing_list(names, sizes, box_size): 
#creates three variables that will be used later
	list = []
	y = 0
	box1 = []
#iterates x over range of names
	for x in range(len(names)):
#if size of name is bigger than maximum size, put it in its own box
		if sizes[x] >= box_size:
			list += [['*' + names[x]]]
#if the last name is reached, return existing list
			if x == len(names) - 1:
				if box1 != []:
					list += [box1]
					return list
				else:
					return list
			continue
#if size of name is equal to max box size, execute and put in own box
		elif sizes[x] == box_size:
			list += [[names[x]]]
			if x == len(names) - 1:
				return list
#if box is filled partially and has more space, execute
		if y > 0:
#if combination of names equals max box size, execute
			if box_sp + sizes[x] == box_size:
				list += [box1 + [names[x]]]
				y = 0
#if the last name is reached, return existing list
				if x == len(names) - 1:
					return list
#if combination of names less than max box size, execute
			elif box_sp + sizes[x] < box_size:
				box_sp += sizes[x]
				box1 += [names[x]]
#if the last name is reached, return existing list
				if x == len(names) - 1:
					list += [box1]
					return list
#if above conditions not met, continue iteration
				else:
					continue
#if combination of names exceeds box capacity, execute
			elif box_sp + sizes[x] > box_size:
#add all names that are less than box size to list, create new list
				list += [box1]
				box_sp = sizes[x]
				box1 = [names[x]]
#if the last name is reached, return existing list
				if x == (len(names) - 1):
					list += [box1]
					return list
#if above conditions not met, continue the loop
				else:
					continue
#if the name gotten can fit in the box, execute and iterate y
		elif sizes[x] < box_size:
			box_sp = sizes[x]
			box1 = [names[x]]
			y += 1