from math import prod

OPEN_SPACE = "."
TREE = "#"


def get_solution(map_grid, slopes):
    tree_counts = [
        count_trees_on_slope(slope[0], slope[1], map_grid) for slope in slopes
    ]
    return prod(tree_counts)


def count_trees_on_slope(slope_x, slope_y, map_grid):
    x_position = 0
    num_trees = 0
    map_width = len(map_grid[0])
    for y_position in range(0, len(map_grid), slope_y):
        if map_grid[y_position][x_position] == TREE:
            num_trees += 1
        x_position = get_x_position(x_position, slope_x, map_width)
    return num_trees


def get_x_position(current_x, increment, map_width):
    thing = current_x + increment
    if thing >= map_width - 1:
        thing -= map_width
    return thing


if __name__ == "__main__":
    input_map = [line.strip() for line in open("input.txt", "r")]
    input_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print(get_solution(input_map, input_slopes))
