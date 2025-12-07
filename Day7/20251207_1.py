from copy import deepcopy

start_x, start_y = -1, -1
total_splits = 0

with open('20251207_input.txt') as f:
    lines = f.readlines()
    first_line, lines = lines[0], lines[1:]
    for i, char in enumerate(first_line):
        if char == 'S':
            start_x = i
            start_y = 0
    
    current_beams = set()
    current_beams.add((start_x, 1))
    for line in lines:
        tmp_beams = deepcopy(current_beams)
        for beam in tmp_beams:
            current_beams.remove(beam)
            if line[beam[0]] == '^':
                if beam[0]-1 >= 0: current_beams.add((beam[0]-1, beam[1]+1))
                if beam[0]+1 < len(line): current_beams.add((beam[0]+1, beam[1]+1))
                total_splits += 1
            else:
                 current_beams.add((beam[0], beam[1]+1))
    
    print(total_splits)