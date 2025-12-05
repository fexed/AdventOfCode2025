total = 0
input_ids = set()
with open('20251205_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            break

        parts = line.split('-')
        new_start = int(parts[0])
        new_end = int(parts[1])
        input_ids.add((new_start, new_end))
    
    fresh_ids = sorted(input_ids)
    merged = []
    for start, end in fresh_ids:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    for start, end in merged:
        total += (end - start + 1)
    print(total)