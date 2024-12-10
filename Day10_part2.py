def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data

def convert_to_2d_list(data):
    return [list(map(int, list(line))) for line in data.split('\n')]

def find_trailheads(map_2d):
    trailheads = []
    for i in range(len(map_2d)):
        for j in range(len(map_2d[i])):
            if map_2d[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(map_2d, x, y, current_height):
    return 0 <= x < len(map_2d) and 0 <= y < len(map_2d[0]) and map_2d[x][y] == current_height + 1

def bfs(map_2d, start):
    queue = [start]
    visited = set()
    visited.add(start)
    score = 0
    
    while queue:
        x, y = queue.pop(0)
        if map_2d[x][y] == 9:
            score += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(map_2d, nx, ny, map_2d[x][y]):
                queue.append((nx, ny))
                visited.add((nx, ny))
    
    return score

def calculate_scores(map_2d, trailheads):
    scores = []
    for trailhead in trailheads:
        score = bfs(map_2d, trailhead)
        scores.append(score)
    return scores

def count_distinct_paths(map_2d, start):
    def dfs(x, y, current_height):
        if map_2d[x][y] == 9:
            return 1
        paths = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(map_2d, nx, ny, current_height):
                paths += dfs(nx, ny, current_height + 1)
        return paths
    
    return dfs(start[0], start[1], 0)

def calculate_ratings(map_2d, trailheads):
    ratings = []
    for trailhead in trailheads:
        rating = count_distinct_paths(map_2d, trailhead)
        ratings.append(rating)
    return ratings

# Hauptprogramm
file_path = 'input.txt'
topographic_map = read_input_file(file_path)
topographic_map_2d = convert_to_2d_list(topographic_map)
trailheads = find_trailheads(topographic_map_2d)

# Teil 1: Berechnung der Scores
scores = calculate_scores(topographic_map_2d, trailheads)
print("Summe der Scores aller Trailheads:", sum(scores))

# Teil 2: Berechnung der Ratings
ratings = calculate_ratings(topographic_map_2d, trailheads)
print("Summe der Ratings aller Trailheads:", sum(ratings))