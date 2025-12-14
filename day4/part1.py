grid = []

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            grid.append(l[:-1])

height = len(grid)
width = len(grid[0])

total = 0
for y in range(height):
    for x in range(width):
        if grid[y][x] == "@":
            nb_around = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0):
                        if 0 <= y + dy < height and 0 <= x + dx < width:
                            if grid[y + dy][x + dx] == "@":
                                nb_around += 1
            if nb_around < 4:
                total += 1
print(total)