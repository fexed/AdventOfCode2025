RANGE_ANALYSIS = 0
FRESH_ANALYSIS = 1

state = RANGE_ANALYSIS

total = 0
fresh_ids = set()
with open('20251205_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            state = FRESH_ANALYSIS
            continue

        if state == RANGE_ANALYSIS:
            parts = line.split('-')
            start = int(parts[0])
            end = int(parts[1])
            fresh_ids.add((start, end))
        elif state == FRESH_ANALYSIS:
            id = int(line)
            for (start, end) in fresh_ids:
                if start <= id <= end:
                    total += 1
                    break
    print(total)