def fill(grid, old_value, new_value, seed):
	hori = seed[0]
	start = 1
	vert = seed[start]
	for x in range(-1, 2, start):
		for y in range(-1, 2, start):
			if hori +x	 in range(len(grid)) and y+vert in range(len(grid[0])):
				if (grid[hori + x][vert+y] == old_value):
					grid[x+hori][y+vert] = new_value
					fill(grid, old_value, new_value, (x+hori, y+vert))
					
def descendants(family_tree, name, distance):
	start = 1
	list = []
	for z in family_tree.keys():
		if name == z:		
			if distance == start:
				return family_tree[name]
			else:
				for x in family_tree[name]:
					distance = distance - start
					list = list + descendants(family_tree,x,distance)
					distance = distance + start
	return list