lst = range(0, 100)

index = 50

zeros = 0
with open('20251201_input.txt') as f:
    for line in f:
        direction = 1 if (line[0] == 'R') else -1
        movement = int(line[1:])
        
        for i in range(movement):
            index = index + direction
            if index >= len(lst):
                index = index % len(lst)
            elif index < 0:
                index = index % len(lst)

        if lst[index] == 0:
            zeros += 1


print(zeros)