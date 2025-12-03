from itertools import combinations
from tqdm import tqdm

with open('20251203_input.txt') as f:
    sum = 0
    for line in tqdm(f):
        # Read a line of digits and put them into a list of integers
        digits = [int(char) for char in line.strip()]
        num = 0
        index = -1
        for i in reversed(range(12)):
            first_max = max(digits[0 if (index == -1) else index + 1:len(digits)-i])
            index = digits.index(first_max, 0 if (index == -1) else index + 1)
            num += first_max * (10 ** (i))
        sum += num

    print(sum)