from copy import deepcopy

start_x, start_y = -1, -1
total_timelines = 0

with open('20251207_input.txt') as f:
    lines = f.readlines()
    first_line, lines = lines[0], lines[1:]
    for i, char in enumerate(first_line):
        if char == 'S':
            start_x = i
            start_y = 0
    
    current_beams = dict()
    current_beams[start_x] = 1
    for line in lines:
        for beam in current_beams.copy():
            if line[beam] == '^':
                if beam - 1 in current_beams:
                    current_beams[beam - 1] += current_beams[beam]
                else:
                    current_beams[beam - 1] = current_beams[beam]
                if beam + 1 in current_beams:
                    current_beams[beam + 1] += current_beams[beam]
                else:
                    current_beams[beam + 1] = current_beams[beam]
                current_beams.pop(beam)
    
    for beam in current_beams:
        total_timelines += current_beams[beam]
    print(total_timelines)