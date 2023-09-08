import copy

OPEN = " "
OUTER_WALL = "#"
INNER_WALL = "@"
BEGIN = "R"
END = "T"
FLOW = ["↑", "→", "↓", "←"]
ROUTE = ["☝", "☞", "☟", "☜"]

DIRECTION = 4

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

MAP = [
    [
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
    ],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OUTER_WALL],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, INNER_WALL, OPEN, OUTER_WALL],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, INNER_WALL, END, OUTER_WALL],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        INNER_WALL,
        INNER_WALL,
        INNER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        OPEN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [
        OUTER_WALL,
        BEGIN,
        INNER_WALL,
        OPEN,
        OPEN,
        OPEN,
        OPEN,
        INNER_WALL,
        OPEN,
        OUTER_WALL,
    ],
    [OUTER_WALL, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OPEN, OUTER_WALL],
    [
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
        OUTER_WALL,
    ],
]

DIFFERENCE = [[-1, 0], [0, 1], [1, 0], [0, -1]]

temp = 0


def main():
    print_map(MAP)
    end_coordinate = get_end(MAP)
    result_map = create_flow(MAP, end_coordinate, temp)
    print_map(result_map)

    return


def is_square_matrix(map_matrix):
    if len(set([len(row) for row in map_matrix])) == 2:
        return True
        # print("Error:Not a square matrix")
    return False


def print_map(map_matrix):
    for row in map_matrix:
        print(" ".join(row))


def get_end(map_matrix):
    for index, row_list in enumerate(map_matrix):
        if END in row_list:
            return index, row_list.index(END)

    return None


def create_flow(map_matrix, target_coordinate, temp):
    # flow_map = copy.deepcopy(map_matrix)
    flow_map = map_matrix

    temp += 1

    previous_coordinate = target_coordinate

    for i in range(DIRECTION):
        current_coordinate = [
            previous_coordinate[0] + DIFFERENCE[i][0],
            previous_coordinate[1] + DIFFERENCE[i][1],
        ]

        if current_coordinate[0] < 0 or current_coordinate[0] + 1 > len(flow_map):
            continue

        if current_coordinate[1] < 0 or current_coordinate[1] + 1 > len(
            flow_map[current_coordinate[0]]
        ):
            continue

        if (
            flow_map[previous_coordinate[0]][previous_coordinate[1]] not in FLOW
            and flow_map[previous_coordinate[0]][previous_coordinate[1]] != END
        ):
            continue

        if flow_map[current_coordinate[0]][current_coordinate[1]] == OPEN:
            flow_map[current_coordinate[0]][current_coordinate[1]] = FLOW[
                (i + 2) % DIRECTION
            ]

        create_flow(flow_map, current_coordinate, temp)

        if temp > 15:
            return flow_map

    return flow_map


if __name__ == "__main__":
    main()
