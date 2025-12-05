max = 100
index = 50

zeros = 0
with open('20251201_input.txt') as f:
    for line in f:
        direction = 1 if (line[0] == 'R') else -1
        movement = int(line[1:])
        
        t0 = ((-direction * index) % max)
        if t0 == 0:
            t0 = max
        
        if movement >= t0:
            zeros += 1 + (movement - t0) // max
        
        index = (index + direction * movement) % max

print(zeros)