# PYTHON BASICS PROGRAM
#Welcomes the user to the program
print('Welcome to the Cake Slice Program!')
#Stores the imputted type of cake made
cake_flavor = input('What kind of cake did you make? ')
#Stores the imputted length of the cake made
cake_long = int(input('How long is the cake in centimeters? '))
#Stores the imputted width of the cake made
cake_wide = int(input('How wide is the cake in centimeters? '))
#Stores the imputted length of the cake slice
slice_long = int(input('How long will you cut your slices in centimeters? '))
#Stores the imputted width of the cake slice
slice_wide = int(input('How wide will you cut your slices in centimeters? '))
#Stores the total area of the cake
cake_area = cake_long * cake_wide
#Displays the total area of the unsliced cake
print('Your cake has a surface area of', cake_area ,'square centimeters.')
#Stores the number times the slice length fits the entire cake length
cut_slice_length = int(cake_long / slice_long)
#Stores the number times the slice width fits the entire cake width
cut_slice_width = int(cake_wide / slice_wide)
#Stores the highest possible number of cake slices that can be cut
cut_slice = cut_slice_length * cut_slice_width
#Stores the area of a single cake slice
slice_area = slice_long * slice_wide
#Stores the total area of all the cake slices that can be cut
total_slice_area = cut_slice * slice_area
#Stores the total slice area percentage of the entire cake
cake_percent = round((total_slice_area / cake_area) * 100)
#Displays number of cake slices that can be cut with its dimensions
print('You can cut', cut_slice ,'total', end=' ')
print(str(slice_long) + 'x' + str(slice_wide),'slices of cake.')
#Displays total area of all the cake slices and its percentage of whole cake
print('These slice dimensions can cut a total of', total_slice_area, end=' ')
print('square centimeters, or', str(cake_percent) + '%, of the cake.')
#Stores number of leftover cake that cant be used for a slice
cake_waste_area = cake_area - total_slice_area
#Stores the wasted cake area percentage of the entire cake area
cake_waste_percent = round((cake_waste_area / cake_area) * 100)
#Displays the total area of cake wasted and its percentage of entire cake
print('These slice dimensions will waste', cake_waste_area, end=' ') 
print('square centimeters, or', str(cake_waste_percent) + '%, of the cake.')
#Calculates the number of edge pieces from the slices cut
cake_edge = (cut_slice_length * 2) + (cut_slice_width * 2) - 4
#Calculates the number of center pieces from the slices cut
cake_center = cut_slice - cake_edge
#Displays the number of edge pieces to the user
print('There will be', cake_edge, end=' ')
print('edge pieces, and', cake_center,'center pieces of cake.')
#Tells the user to enjoy whatever cake they made in the beginning
print('Enjoy your', cake_flavor, 'cake!')








