def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

def move_forward(position, direction):
    x, y = position
    if direction == '^':
        return (x - 1, y)
    elif direction == '>':
        return (x, y + 1)
    elif direction == 'v':
        return (x + 1, y)
    elif direction == '<':
        return (x, y - 1)

def is_within_bounds(position, map):
    x, y = position
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def predict_guard_path(map):
    # Find the initial position and direction of the guard
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == '^':
                position = (i, j)
                direction = '^'
                break

    visited_positions = set()
    visited_positions.add(position)

    while True:
        next_position = move_forward(position, direction)
        if not is_within_bounds(next_position, map) or map[next_position[0]][next_position[1]] == '#':
            direction = turn_right(direction)
        else:
            position = next_position
            visited_positions.add(position)
            map[position[0]][position[1]] = 'X'

        if not is_within_bounds(next_position, map):
            break

    return len(visited_positions)

# Beispielaufruf
file_path = 'input.txt'  # Pfad zur Eingabedatei
map = read_map(file_path)
distinct_positions = predict_guard_path(map)
print(f"Anzahl der besuchten Positionen: {distinct_positions}")