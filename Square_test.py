import json
import argparse

def bubblesort(my_list):
    for i in range (0, len(my_list) - 1):
        for j in range(0, len(my_list) -1 -i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
parser = argparse.ArgumentParser('Input Coordinate File')
parser.add_argument('-r', '--read', required=True, type=str, help= 'enter file to be read')
args, unknown = parser.parse_known_args()

file = args.read
f = open(file)

data = json.load(f)


x_list = []
y_list = []

for x in data:
    x_list.append(data[x]['x'])
for y in data:
    y_list.append(data[y]['y'])
print("coordinates inputed: ")
for z in data:
    print(data[z])

x_list = bubblesort(x_list)
y_list = bubblesort(y_list)

bottom_left = [x_list[0],y_list[0]]
top_right = [x_list[len(x_list)-1], y_list[len(y_list)-1]]
top_left = [bottom_left[0], top_right[1]]
bottom_right = [top_right[0], bottom_left[1]]

# print(bottom_left)
# print(top_right)
# print(top_left)
# print(bottom_right)
#
parallel_x_len = top_right[0] - top_left[0]
parallel_y_len = top_left[1] - bottom_left[1]
#
# print(parallel_x_len)
# print(parallel_y_len)

if parallel_y_len < parallel_x_len:
    # print("width is running")
    difference_len = (parallel_x_len - parallel_y_len)/2
    bottom_left[1] -= difference_len
    bottom_right[1] -= difference_len
    top_left[1] += difference_len
    top_right[1] += difference_len
else:
    # print("height is running")
    difference_len = (parallel_y_len - parallel_x_len) / 2
    print(f"difference in lenght: {difference_len}")
    bottom_left[0] -= difference_len
    bottom_right[0] += difference_len
    top_left[0] -= difference_len
    top_right[0] += difference_len
print("\nThe coordinates of the smallest possible square surrounding these coordinates are: ")
print(f"top right coordinate: {top_right}")
print(f"top left coordinate: {top_left}")
print(f"bottom right coordinate: {bottom_right}")
print(f"bottom left coordinate: {bottom_left}")

parallel_x_len = top_right[0] - top_left[0]
parallel_y_len = top_left[1] - bottom_left[1]
print(f"\nThe length of each side of this square is: {round(parallel_x_len, 3)}")

f.close()
