#defines the histogram function
def histogram(image):
#creates variables to be used later in the function
    count = 0
    final = []
    i = 0
    z = 0
#iterates for every number from 0 to 255
    for int in range(0, 256):
#if i is on its final iteration, execute
        if i == len(image[z - 1]):
#appends the number of count to the larger list
            final.append(count)
            count = 0
            z = 0
#iterates each sublist in image
        for list in image:
#creates variables to be used later in the function
            z +=1
            i = 0
#iterates through each number inside the sublist
            for num in list:
#if the iterated number is in the number from 0-255, increment count
                if int == num:
                    count += 1
                    i += 1
                    continue
                i += 1
# if i has iterated across all the lists, break
                if i == len(image[z - 1]):
                    break
#adds the last count value to the final output, then return
    final.append(count)
    return final

#defines the flip function with 2 paramters
def flip(image, orientation):
#creates a set of variables to be used later
    i = 0
    z = 0
    x = image.copy()
#if true, execute
    if orientation == 'horizontal':
#creates a while loop that executes while i is inside x
        while x[i] in x:
#for each num from reversed copy of image (x)
            for num in x[i][::-1]:
#replaces the value inside image with the reversed order number
                image[i][z] = num
                z += 1
#if the final list has been iterated, execute
                if z == len(x[i]):
                    z = 0
                    i += 1
#if the final list has been iterated, return none	
                    if i == len(image):
                        return None
                    continue
#if the orientation is vertical, reverse each sublist in image
    if orientation == 'vertical':
        for sublist in image:
            i += 1
        x = x[::-1]
#replace image with its reversed sublists
        image[0:i] = x

#defines the rotate function
def rotate(image):
#creates variables to be used later
	i = 0
	list = image[:]
	nums = len(image)
#iterates through each column in image
	for cols in range(0, nums, 1):
		i += 1
#when square is rotated replace (1st row, last col, 2nd row, middle colum...)
		for int in range(nums - 1, -1, -1):
			list[cols] = image[int]
			if cols >= 0:
				cols = cols + 1
#if all nums been iterated through, delete duplicate image and exit loop
		if int == 0:
			del image[:]
			break
	a = 0
#for each sublist in the copy of image
	for x in list:
		nums2 = len(x)
#iterates through each column in image
		for cols in range(0, nums2, 1):
			a += 1
			inner = []
#for each iteration through list length, add the col index value in list[y]
			for y in range(0, len(list), 1):
				inner.append(list[y][cols])
			image.append(inner)
		break

#defines the crop function	
def crop(image, origin, height, width):
#creates variables to be used later
    outer = []
    i = 0
#determines which row the origin will begin from
    x = origin[i]
    inner = []
#determines which column the origin will begin from
    y = origin[1]
#creates a loop that iterates through the rows
    for nums1 in range(x, x + height, 1):
#creates a loop that iterates through the columns
        for nums2 in range(y, y + width, 1):
#appends the matched location in the list to inner
            inner.append(image[nums1][nums2])
#appends the inner list to the outer list, then restarts empty
        outer.append(inner)
        inner = []
    return outer

#defines the color2gray function	
def color2gray(image):
#creates variables to be used later
    quan = 0
    i = 0
    inner = []
    outer = []
#creates a loop that iterates through each sublist in image
    for sublist in image:
        i = 0
#if inner has values inside, append to outer
        if inner != []:
            outer.append(inner)
            inner = []
#creates a loop for each list in sublist
        for list in sublist:
#creates a loop for each num in list
            for nums in list:
#gets total val of the list and adds 1 to quantity for each val in list
                total = sum(list)
                quan += 1
#once every value iterate, appends average to inner list
                if quan == len(list):
                    average = int(total / quan)
                    inner.append(average)
                    i += 1
                    quan = 0
                    total = 0
#apends final inner to outer and returns outer
    outer.append(inner)
    return outer

#defines the extract_layer function
def extract_layer(image, color):
#creates variables to be used later
    outer = []
    inner = []
    i = 0
    z = 0
#if the color is red, append 1st value of innermost list to inner
    if color == 'red':
        for sublist in image:
            for list in sublist:
                for nums in list:
                    inner.append(nums)
                    i += 1
#appends each group of inner lists to the outer list, then break
                    if i == len(sublist):
                        outer.append(inner)
                        i = 0
                        inner = []
                    break
#if the color is green, append 2nd value of innermost list to inner
    if color == 'green':
        for sublist in image:
            for list in sublist:
#appends each group of inner lists to the outer list
                if z == len(sublist):
                    outer.append(inner)
                    i = 0
                    z = 0
                    inner = []
                z += 1
#gets the 2nd value in the group of 3 then appends that to the inner list
                for nums in list:
                    i += 1
                    if i == 2:
                        inner.append(nums)
                        i = 0
                        break
#appends each group of inner lists to the outer list
        if z == len(sublist):
            outer.append(inner)
            i = 0
            z = 0
            inner = []
#if the color is blue, append 3rd value of innermost list to inner
    if color == 'blue':
        for sublist in image:
            for list in sublist:
#appends each group of inner lists to the outer list
                if z == len(sublist):
                    outer.append(inner)
                    i = 0
                    z = 0
                    inner = []
                z += 1
#gets the 2nd value in the group of 3 then appends that to the inner list
                for nums in list:
                    i += 1
                    if i == 3:
                        inner.append(nums)
                        i = 0
                        break
#appends each group of inner lists to the outer list
        if z == len(sublist):
            outer.append(inner)
            i = 0
            z = 0
            inner = []
#returns final output outer
    return outer

#defines the scale function
def scale(image, factor):
    list = []
    i = 0
    y = 1
    b = 0
    z = 0
    a = 0
#if the factor is positive, execute
    if factor > 0:
#if y has been incremented, execute
        for sublist in image:
            if y != 1:
                i += 1
#iterates through image and creates new memory of that list
            copylist = image[i][:]
            a = 0
#if all values of copylist iterated, append it to list
            if b == len(copylist):
                while z < factor:
                    z += 1
                    list.append(add)
                z = 0
                b = 0
#iterates through each number in the copylist
            for nums in copylist:
                    y = 1
                    b += 1
#inserts a duplicate of the number until it reaches the number of factor
                    while y < factor:
                        if y == 1:
                            sublist.insert(a, nums)
                            a += 2
                            y += 1
                            add = sublist
                            continue
                        sublist.insert(a, nums)
                        a += 1
                        y += 1
                        add = sublist
#replaces contenets of imput list with the changed list
        while z < factor:
            z += 1
            list.append(add)
        image[0:len(image)] = list

#defines the compress function
def compress(image):
#creates variables that will be used later
    outer = []
    inner = []
    count1 = 0
    count2 = 0
    i = 0
#creates a loop that iterates through each sublist in image
    for sublist in image:
        i = 0
#iterates through each value in the sublist
        for vals in sublist:
#if the count is 0 and val is white, append and increment count
            if i == 0 and vals >= 128:
                inner.append(0)
            i += 1
#if the count has started and value continues to be white, increment count
            while vals >= 128:
                count1 += 1
                if i >= len(sublist):
                    inner.append(count1)
                    break
#if the next value is black, append white count1 and restart
                elif sublist[i] <= 127:
                    inner.append(count1)
                    count1 = 0
                break
#if the value is black
            while vals <= 127:
                count2 += 1
#if all vals iterated through sublist, append and break
                if i >= len(sublist):
                    inner.append(count2)
                    break
#if the next value is white, append black count2 and restart		
                if sublist[i] >= 128:
                    inner.append(count2)
                    count2 = 0
                break
#if final iteration of sublist, restart both count and append inner to outer
            if i == len(sublist):
                count1 = 0
                count2 = 0
                outer.append(inner)
                inner = []
#returns final output outer
    return outer

#defines the median_filter
def median_filter(image):
#creates variables that will be used later
    list = []
    start = 0
    inner = []
    outer = []
    i = 0
#iterates through the number of colums except last one
    for x in range(start + 1, len(image) - 1, 1):
#appends an inner list to the outer list
        list.append(inner)
#iterates through each value except last column
        for y in range(start + 1, len(image[0]) - 1, 1):
#sorts every pixel value in the 3x3 range of area around the middle value
            median_1 = sorted([image[x-1][y],image[x+1][y+1]])
            median_2 = sorted([image[x+1][y-1],image[x-1][y-1],image[x][y]])
            median_3 = sorted([image[x][y-1],image[x][y+1],image[x+1][y]])
            median_4 = sorted([image[x-1][y+1]])
#finds the median value of all the vals in the 3x3 grind and appends to list
            final = sorted(median_1 + median_2 + median_3 + median_4)
            list[i].append(final[len(final) // 2])
        inner = []
#increments through each index in the list
        if i == 0:
            i += 1
        elif i != 0:
            i += 1
#returns the final list with all the median values
    return list
