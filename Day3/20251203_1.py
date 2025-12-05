with open('20251203_input.txt') as f:
    sum = 0
    for line in f:
        # Read a line of digits and put them into a list of integers
        digits = [int(char) for char in line.strip()]
        first_max = max(digits[:len(digits)-1])
        index_of_first_max = digits.index(first_max)
        second_max = max(digits[index_of_first_max + 1:])
        sum += first_max*10 + second_max

    print(sum)