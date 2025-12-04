from copy import deepcopy

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

    tmpSum = 0
    tmpGrid = deepcopy(grid)
    while True:
        
        for y in range(len(tmpGrid)):
            for x in range(len(tmpGrid[0])):
                if tmpGrid[y][x] == '@':
                    if check(tmpGrid, x, y):
                        tmpSum += 1
                        grid[y][x] = 'x'
        if tmpSum == 0:
            break
        else:
            tmpGrid = deepcopy(grid)
            sum += tmpSum
            tmpSum = 0
    
    print(sum)
    