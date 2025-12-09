def area(first, second):
    return (abs(first[0] - second[0]) + 1) * (abs(first[1] - second[1]) + 1)


coords = []

with open('20251209_input.txt') as f:
    for line in f:
        parts = line.strip().split(',')
        x, y = int(parts[0]), int(parts[1])
        coords.append((x, y))
    
    ans = None
    biggest_area = 0
    for curr_x, curr_y in coords:
        for target_x, target_y in coords:
            a = area((curr_x, curr_y), (target_x, target_y))
            if a > biggest_area:
                ans = [(curr_x, curr_y), (target_x, target_y)]
                biggest_area = a
    
    print(area(ans[0], ans[1]))
    
