def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data

def convert_to_2d_list(data):
    lines = data.split('\n')
    topographic_map = [list(map(int, line)) for line in lines]
    return topographic_map

def find_trailheads(topographic_map):
    trailheads = []
    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[i])):
            if topographic_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(topographic_map, x, y, next_x, next_y):
    if 0 <= next_x < len(topographic_map) and 0 <= next_y < len(topographic_map[0]):
        return topographic_map[next_x][next_y] == topographic_map[x][y] + 1
    return False

def find_paths(topographic_map, start_x, start_y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(start_x, start_y)]
    visited = set()
    paths_to_nine = 0

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if topographic_map[x][y] == 9:
            paths_to_nine += 1
            continue

        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if is_valid_move(topographic_map, x, y, next_x, next_y):
                stack.append((next_x, next_y))

    return paths_to_nine

def calculate_total_score(trailhead_scores):
    return sum(trailhead_scores)

# Hauptprogramm
file_path = 'input.txt'  # Pfad zur Eingabedatei
input_data = read_input_file(file_path)
topographic_map = convert_to_2d_list(input_data)
trailheads = find_trailheads(topographic_map)
trailhead_scores = [find_paths(topographic_map, x, y) for x, y in trailheads]
total_score = calculate_total_score(trailhead_scores)

print("Gesamtscore aller Trailheads:")
print(total_score)