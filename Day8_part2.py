def read_input(file_path):
    """
    Liest die Karte aus einer Datei ein und speichert sie als Liste von Strings.
    
    Args:
        file_path (str): Pfad zur Eingabedatei.
        
    Returns:
        list[str]: Liste von Strings, die die Karte repräsentieren.
    """
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

# Beispielaufruf
file_path = "antenna_map.txt"  # Datei mit dem mehrzeiligen String
map_data = read_input(file_path)
print("Karte eingelesen:")
print("\n".join(map_data))

def find_antennas(map_data):
    """
    Identifiziert die Positionen und Frequenzen aller Antennen in der Karte.

    Args:
        map_data (list[str]): Liste von Strings, die die Karte repräsentieren.

    Returns:
        dict[str, list[tuple[int, int]]]: Ein Dictionary, bei dem die Schlüssel die Frequenzen
                                          sind und die Werte Listen von Koordinaten (x, y).
    """
    antennas = {}
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char.isalnum():  # Prüft, ob der Charakter eine Antenne (Buchstabe/Zahl) ist
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

# Beispielaufruf
antennas = find_antennas(map_data)
print("Gefundene Antennen:")
for frequency, positions in antennas.items():
    print(f"Frequenz '{frequency}': {positions}")


def calculate_antinodes_part1(map_data, antennas):
    """
    Berechnet die Antinoden für Part 1, basierend auf der 1:2-Entfernungsregel.

    Args:
        map_data (list[str]): Liste von Strings, die die Karte repräsentieren.
        antennas (dict[str, list[tuple[int, int]]]): Positionen der Antennen nach Frequenz.

    Returns:
        set[tuple[int, int]]: Eine Menge aller eindeutigen Antinoden innerhalb der Kartenbegrenzung.
    """
    width = len(map_data[0])
    height = len(map_data)
    antinodes = set()

    for frequency, positions in antennas.items():
        # Prüfe alle Paare von Antennen mit derselben Frequenz
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Berechne den Abstand zwischen den Antennen
                dx = x2 - x1
                dy = y2 - y1

                # Prüfe die 1:2-Entfernungsregel
                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                # Füge Antinoden hinzu, falls sie innerhalb der Karte liegen
                if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                    antinodes.add(antinode2)

    return antinodes

# Beispielaufruf
antinodes_part1 = calculate_antinodes_part1(map_data, antennas)
print(f"Anzahl eindeutiger Antinoden (Part 1): {len(antinodes_part1)}")

def calculate_antinodes_part2(map_data, antennas):
    """
    Berechnet die Antinoden für Part 2, basierend auf der erweiterten Regel (1:n),
    einschließlich der Ausnahme für Antennenpositionen.

    Args:
        map_data (list[str]): Liste von Strings, die die Karte repräsentieren.
        antennas (dict[str, list[tuple[int, int]]]): Positionen der Antennen nach Frequenz.

    Returns:
        set[tuple[int, int]]: Eine Menge aller eindeutigen Antinoden innerhalb der Kartenbegrenzung.
    """
    width = len(map_data[0])
    height = len(map_data)
    antinodes = set()

    for frequency, positions in antennas.items():
        # Prüfe alle Paare von Antennen mit derselben Frequenz
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Berechne den Abstand zwischen den Antennen
                dx = x2 - x1
                dy = y2 - y1

                # Für n = 2, 3, 4, ..., solange die Antinoden innerhalb der Karte bleiben
                n = 2
                while True:
                    antinode1 = (x1 - dx * (n - 1), y1 - dy * (n - 1))
                    antinode2 = (x2 + dx * (n - 1), y2 + dy * (n - 1))

                    added = False
                    # Füge Antinode1 hinzu, falls innerhalb der Karte
                    if 0 <= antinode1[0] < width and 0 <= antinode1[1] < height:
                        antinodes.add(antinode1)
                        added = True
                    # Füge Antinode2 hinzu, falls innerhalb der Karte
                    if 0 <= antinode2[0] < width and 0 <= antinode2[1] < height:
                        antinodes.add(antinode2)
                        added = True

                    # Breche die Schleife ab, wenn keine neuen Antinoden gefunden wurden
                    if not added:
                        break

                    n += 1

        # Prüfe, ob jede Antenne selbst als Antinode zählt
        for x, y in positions:
            same_line_count = sum(
                1
                for other_x, other_y in positions
                if (other_x - x) * (y - other_y) == (other_y - y) * (x - other_x) and (x, y) != (other_x, other_y)
            )
            if same_line_count >= 2:
                antinodes.add((x, y))

    return antinodes

# Beispielaufruf
antinodes_part2 = calculate_antinodes_part2(map_data, antennas)
print(f"Anzahl eindeutiger Antinoden (Part 2): {len(antinodes_part2)}")
