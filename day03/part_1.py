
OPEN_SPACE = "."
TREE = "#"
X_AXIS_MOVE = 3
Y_AXIS_MOVE = 1


def traverse(map_grid, x_move, y_move):
    x_position = 0
    num_trees = 0
    map_width = len(map_grid[0])
    for y_position in range(0, len(map_grid), y_move):
        if map_grid[y_position][x_position] == TREE:
            num_trees += 1
        x_position = get_x_position(x_position, x_move, map_width)
    print(f"I hit {num_trees} trees")


def get_x_position(current_x, increment, map_width):
    position = current_x + increment
    if position >= map_width:
        position -= map_width
    return position


if __name__ == '__main__':
    input_map = [line.strip() for line in open("input.txt", "r")]
    traverse(input_map, X_AXIS_MOVE, Y_AXIS_MOVE)
