import json
import argparse
import sys
import os

#Expected keys which are constant
X_KEY = 'x'
Y_KEY = 'y'

#Bubblesort function to get x and y coordinates from smallest to largest to figure out top left and bottom right of
#the square
def bubblesort(my_list):
    for i in range (0, len(my_list) - 1):
        for j in range(0, len(my_list) -1 -i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
#unpacks data from json file into appropriate x and y coordinate lists
def unpack(data, key):
    orderlist = []
    for x in data:
        orderlist.append(data[x][key])
    return orderlist
#create the square
def create_Square(x_coor, y_coor):
    bottom_left = [x_coor[0], y_coor[0]]
    top_right = [x_coor[len(x_coor) - 1], y_coor[len(y_coor) - 1]]
    top_left = [bottom_left[0], top_right[1]]
    bottom_right = [top_right[0], bottom_left[1]]

    parallel_x_len = top_right[0] - top_left[0]
    parallel_y_len = top_left[1] - bottom_left[1]

    if parallel_y_len < parallel_x_len:
        # print("width is running")
        difference_len = (parallel_x_len - parallel_y_len) / 2
        bottom_left[1] -= difference_len
        bottom_right[1] -= difference_len
        top_left[1] += difference_len
        top_right[1] += difference_len
    else:
        # print("height is running")
        difference_len = (parallel_y_len - parallel_x_len) / 2
        bottom_left[0] -= difference_len
        bottom_right[0] += difference_len
        top_left[0] -= difference_len
        top_right[0] += difference_len

    square_corners = {
        "Top_Left":
            {
                "x": top_left[0],
                "y": top_left[1]
            },
        "Bottom_Right":
            {
                "x": bottom_right[0],
                "y": bottom_right[1]
            },
        "Bottom_Left":
            {
                "x": bottom_left[0],
                "y": bottom_left[1]
            },
        "Top_Right":
            {
                "x": top_right[0],
                "y": top_right[1]
            },
        "Each side Length": top_right[0] - top_left[0]
    }
    return square_corners
#error handling if file does not exist
def read_file(file):

    try:
        f = open(file)
    except FileNotFoundError:
        print(f"File {file} not found.  Aborting")
        sys.exit(1)

    if os.stat(file).st_size == 0:
        print("Empty File")
        sys.exit(1)

    elif not file.endswith(".json"):
        print("not a JSON File")
        sys.exit(1)
    else:
        return f
#error handling if keys are incorrect
def incorrect_keys(data):
    try:
        for x in data:
            return int(data[x]['x'])
    except KeyError:
        print("Missing X coordinate key in file. Aborting")
        sys.exit(1)
    except ValueError:
        print("Only Numeric Values can be entered as coordinates. Aborting")
        sys.exit(1)
    try:
        for x in data:
            return int(data[x]['y'])
    except KeyError:
        print("Missing Y coordinate key in file. Aborting")
        sys.exit(1)
    except ValueError:
        print("Only Numeric Values can be entered as coordinates. Aborting")
        sys.exit(1)



parser = argparse.ArgumentParser('Input Coordinate File')
parser.add_argument('-r', '--read', required=True, type=str, help= 'enter file to be read')
args, unknown = parser.parse_known_args()

#read json file
file = args.read


data = json.load(read_file(file))
incorrect_keys(data)

#Sorted list of x and y coordinates to figure out best points for square corners
sorted_x_coor_list = bubblesort(unpack(data, X_KEY))
sorted_y_coor_list = bubblesort(unpack(data, Y_KEY))

#create the square
Square = create_Square(sorted_x_coor_list,sorted_y_coor_list)
print("\ncoordinates inputed: ")
for coordinates in data:
    print(data[coordinates])

print("\nThe smallest square that will fit your coordinates has the following coordinates: ")
for key, value in Square.items():
    print(key, ': ', value)




