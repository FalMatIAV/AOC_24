def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes_part1(antennas, width, height):
    antinodes = set()  # Set zur Speicherung der eindeutigen Antinode-Positionen
    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue  # Wenn es weniger als 2 Antennen derselben Frequenz gibt, überspringen
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                if x1 == x2:  # Vertikale Linie
                    if abs(y2 - y1) % 2 == 0:
                        mid_y = (y1 + y2) // 2
                        if 0 <= mid_y < height:
                            antinodes.add((x1, mid_y))
                            print(f"Vertikale Linie: Antenne1=({x1},{y1}), Antenne2=({x2},{y2}), mid_y={mid_y}")
                elif y1 == y2:  # Horizontale Linie
                    if abs(x2 - x1) % 2 == 0:
                        mid_x = (x1 + x2) // 2
                        if 0 <= mid_x < width:
                            antinodes.add((mid_x, y1))
                            print(f"Horizontale Linie: Antenne1=({x1},{y1}), Antenne2=({x2},{y2}), mid_x={mid_x}")
                else:  # Diagonale Linie
                    if abs(x2 - x1) % 2 == 0 and abs(y2 - y1) % 2 == 0:
                        mid_x = (x1 + x2) // 2
                        mid_y = (y1 + y2) // 2
                        if 0 <= mid_x < width and 0 <= mid_y < height:
                            antinodes.add((mid_x, mid_y))
                            print(f"Diagonale Linie: Antenne1=({x1},{y1}), Antenne2=({x2},{y2}), mid_x={mid_x}, mid_y={mid_y}")
    return antinodes

def calculate_antinodes_part2(antennas, width, height):
    antinodes = set()  # Set zur Speicherung der eindeutigen Antinode-Positionen
    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue  # Wenn es weniger als 2 Antennen derselben Frequenz gibt, überspringen
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                if x1 == x2:  # Vertikale Linie
                    for y in range(min(y1, y2) + 1, max(y1, y2)):
                        if 0 <= y < height:
                            antinodes.add((x1, y))
                elif y1 == y2:  # Horizontale Linie
                    for x in range(min(x1, x2) + 1, max(x1, x2)):
                        if 0 <= x < width:
                            antinodes.add((x, y1))
                else:  # Diagonale Linie
                    dx = 1 if x2 > x1 else -1
                    dy = 1 if y2 > y1 else -1
                    for k in range(1, abs(x2 - x1)):
                        mid_x = x1 + k * dx
                        mid_y = y1 + k * dy
                        if 0 <= mid_x < width and 0 <= mid_y < height:
                            antinodes.add((mid_x, mid_y))
        for pos in positions:
            antinodes.add(pos)  # Fügen Sie die Positionen der Antennen selbst als Antinodes hinzu
    return antinodes

def main():
    filename = 'input.txt'
    grid = read_input_file(filename)
    width = len(grid[0])
    height = len(grid)
    antennas = find_antennas(grid)
    
    # Part 1
    antinodes_part1 = calculate_antinodes_part1(antennas, width, height)
    print(f"Part 1 - Number of unique antinode locations: {len(antinodes_part1)}")
    
    # Part 2
    antinodes_part2 = calculate_antinodes_part2(antennas, width, height)
    print(f"Part 2 - Number of unique antinode locations: {len(antinodes_part2)}")

if __name__ == "__main__":
    main()