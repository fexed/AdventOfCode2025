def check(grid: list[list[str]], x: int, y: int) -> bool:
    current = grid[y][x]
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == '@':
                count += 1
    return count < 4

with open('20251204_input.txt') as f:
    sum = 0
    grid = []
    for line in f:
        grid.append([char for char in line.strip()])
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                if check(grid, x, y):
                    sum += 1
    print(sum)
    