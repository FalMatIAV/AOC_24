def count_word_occurrences(grid, word):
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),  # horizontal right
        (1, 0),  # vertical down
        (1, 1),  # diagonal down-right
        (1, -1), # diagonal down-left
        (0, -1), # horizontal left
        (-1, 0), # vertical up
        (-1, -1),# diagonal up-left
        (-1, 1)  # diagonal up-right
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    count += 1
    return count

def main():
    # Read the input string from a file
    with open("input.txt", "r") as file:
        input_string = file.read().strip()

    # Split the input string into lines to create a 2D grid
    grid = [list(line) for line in input_string.split("\n")]
    word = "XMAS"
    result = count_word_occurrences(grid, word)
    print("Number of times XMAS appears:", result)

if __name__ == "__main__":
    main()