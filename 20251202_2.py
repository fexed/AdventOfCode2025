def has_repeated_sequence(num):
    s = str(num)
    for length in range(1, len(s) // 2 + 1):
        tmp = s.replace(s[0:length], '')
        if tmp == '':
            print(f"Found repeated sequence in {num}: {s[0:length]}")
            return True
    return False

with open('20251202_input.txt') as f:
    content = f.read()
    ranges = content.split(',')
    invalid_sum = 0
    for rng in ranges:
        a, b = map(int, rng.split('-'))
        
        for num in range(a, b + 1):
            if has_repeated_sequence(num):
                invalid_sum += num

print(invalid_sum)