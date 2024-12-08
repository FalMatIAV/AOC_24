def read_lab_map_from_file(filename):
    """
    Liest die Karte aus der Datei und gibt sie als Liste von Listen zurück.
    Dabei wird der Wächter erkannt und seine Position und Richtung zurückgegeben.
    """
    lab_map = []
    guard_position = None
    guard_direction = None

    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            line = line.rstrip('\n')
            lab_map_row = list(line)
            # Suche nach dem Wächterzeichen und bestimme Position und Richtung
            for col, char in enumerate(lab_map_row):
                if char in '^v<>':  # Wächterzeichen gefunden
                    guard_position = (row, col)
                    guard_direction = char
            lab_map.append(lab_map_row)

    return lab_map, guard_position, guard_direction


def move_guard_and_check_for_loop(lab_map, start_position, start_direction):
    """
    Simuliert den Wächterzug und prüft, ob der Wächter in eine Schleife gerät.
    Gibt True zurück, wenn der Wächter in eine Schleife gerät, andernfalls False.
    """
    # Bewegungsrichtungen (up, right, down, left)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    current_position = start_position
    current_direction = start_direction
    visited_positions = set()  # Verfolgt alle besuchten Positionen
    visited_with_directions = set()  # Verfolgt Positionen mit Richtungen

    while True:
        # Wenn der Wächter bereits diese Position mit derselben Richtung besucht hat, ist er in einer Schleife
        if (current_position, current_direction) in visited_with_directions:
            return True  # Schleife gefunden

        # Markiere die aktuelle Position und Richtung als besucht
        visited_with_directions.add((current_position, current_direction))

        # Berechne die nächste Position basierend auf der aktuellen Richtung
        move_row, move_col = directions[current_direction]
        next_position = (current_position[0] + move_row, current_position[1] + move_col)

        # Überprüfe, ob die nächste Position außerhalb des Labors oder ein Hindernis ist
        if not (0 <= next_position[0] < len(lab_map) and 0 <= next_position[1] < len(lab_map[0])):
            return False  # Wächter verlässt das Labor
        if lab_map[next_position[0]][next_position[1]] == '#':
            # Wände blockieren den Wächter, er dreht sich nach rechts
            direction_order = ['^', '>', 'v', '<']
            current_direction = direction_order[(direction_order.index(current_direction) + 1) % 4]
        else:
            # Keine Wand, Wächter bewegt sich vorwärts
            current_position = next_position

    return False  # Keine Schleife gefunden


def find_possible_obstruction_positions(lab_map, guard_position, guard_direction):
    """
    Findet alle möglichen Positionen, an denen ein Hindernis gesetzt werden kann, 
    sodass der Wächter in einer Schleife gefangen wird.
    """
    possible_positions = []

    # Alle Positionen auf der Karte durchsuchen
    for row in range(len(lab_map)):
        for col in range(len(lab_map[0])):
            # Sicherstellen, dass die Position nicht die Startposition des Wächters ist
            if (row, col) != guard_position and lab_map[row][col] == '.':
                # Kopiere die Karte und setze an der aktuellen Position ein Hindernis
                modified_map = [list(r) for r in lab_map]
                modified_map[row][col] = '#'

                # Simuliere den Wächterzug mit der neuen Hindernisposition
                if move_guard_and_check_for_loop(modified_map, guard_position, guard_direction):
                    possible_positions.append((row, col))

    return possible_positions


# Beispiel-Input
filename = 'lab_map.txt'  # Der Dateiname der Textdatei
lab_map, guard_position, guard_direction = read_lab_map_from_file(filename)  # Laborkarte aus Datei lesen

print(f"Startposition des Wächters: {guard_position} mit Richtung {guard_direction}")

# Finde mögliche Hindernispositionen
possible_obstruction_positions = find_possible_obstruction_positions(lab_map, guard_position, guard_direction)

print("Mögliche Hindernispositionen:", possible_obstruction_positions)
print("Anzahl möglicher Hindernispositionen:", len(possible_obstruction_positions))

# Wenn du später die Positionen anzeigen möchtest, kannst du die Zeile darunter entkommentieren:
# print("Mögliche Hindernispositionen:", possible_obstruction_positions)
