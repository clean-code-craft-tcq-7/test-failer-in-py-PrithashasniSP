def get_pair_number(major, minor):
    return major * 5 + minor + 1


def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(get_pair_number(0,0) == 1)
assert(get_pair_number(0,1) == 2)
assert(get_pair_number(1,0) == 6)
assert(get_pair_number(4,4) == 25)
print("All is well (maybe!)")
