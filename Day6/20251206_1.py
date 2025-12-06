ADDITION, MULTIPLICATION = 0, 1

with open('20251206_input.txt') as f:
    operators = []
    for line in f:
        parts = line.split()
        operators.append(parts)

    number_of_operations = len(operators[0])
    total = 0
    for i in range(number_of_operations):
        result = 0
        current_operation = ADDITION
        for lst in reversed(operators):
            if lst[i] == '+':
                result = 0
                current_operation = ADDITION
            elif lst[i] == '*':
                result = 1
                current_operation = MULTIPLICATION
            else:
                if current_operation == ADDITION:
                    result += int(lst[i])
                elif current_operation == MULTIPLICATION:
                    result *= int(lst[i])
        total += result
    
    print(total)