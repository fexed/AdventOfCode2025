ADDITION, MULTIPLICATION = 0, 1

with open('20251206_input.txt') as f:
    lines = []
    for line in f:
        lines.append(line[:-1])
    
    start_indexes = []
    for i, char in enumerate(lines[-1]):
        if char != ' ': start_indexes.append(i)
    
    operators = []
    numbers = []
    digits = len(lines) - 1
    for i, index in enumerate(start_indexes):
        curr_numbers = []
        curr_index = index
        while True:
            num = ''
            for pow in range(digits):
                char = lines[pow][curr_index]
                if (char != ' '):
                    num += char
            if (num != ''): curr_numbers.append(int(num))
            curr_index += 1
            if (curr_index >= len(lines[0])): break
            if (i+1 < len(start_indexes)):
                if (curr_index == start_indexes[i+1]): break
        numbers.append(curr_numbers)
        operators.append(lines[-1][index])
    
    total = 0
    result = 0
    
    for op, nums in zip(operators, numbers):
        if op == '+':
            curr = 0
            for n in nums:
                curr += n
        elif op == '*':
            curr = 1
            for n in nums:
                curr *= n
        total += curr
    
    print(total)