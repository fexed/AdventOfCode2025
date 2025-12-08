from itertools import combinations
import math


circuits = []
coord_list = set()


def distance(first, second):
    d1 = first[0] - second[0]
    d2 = first[1] - second[1]
    d3 = first[2] - second[2]
    return math.sqrt(d1**2 + d2**2 + d3**2)


def check_presence(to_check, circuit):
    for coord in circuit:
        if coord == to_check: return True
    return False


def remove_dups(circuit):
    return list(set(circuit))


def merge_circuits(circuits):
    lst = circuits.copy()
    res = []
    while len(lst) > 0:
        first, rest = lst[0], lst[1:]
        first = set(first)
        
        len_first = -1
        while len(first) > len_first:
            len_first = len(first)
            rest2 = []
            for r in rest:
                if (len(first.intersection(set(r)))) > 0:
                    first |= set(r)
                else:
                    rest2.append(r)
            rest = rest2
        res.append(list(first))
        lst = rest
    return res



def clean_circuits(circuits):
    for circuit in circuits:
        circuit = remove_dups(circuit)
    
    circuits = merge_circuits(circuits)

    circuits.sort(key = lambda x : [len(x), x[0]], reverse = True)

    return circuits


with open('20251208_input.txt') as f:
    for line in f:
        parts = line.strip().split(',')
        x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
        coord_list.add((x, y, z))

    pairs = set(combinations(coord_list, 2))

    for i in range(1000):
        min_dist = float('inf')
        closest_pair = None
        for first, second in pairs:
            dist = distance(first, second)
            if dist < min_dist:
                closest_pair = (first, second)
                min_dist = dist
        pairs.remove(closest_pair)
        if len(circuits) == 0:
            circuits.append([closest_pair[0], closest_pair[1]])
        else:
            added = False
            for i, circuit in enumerate(circuits):
                if check_presence(closest_pair[0], circuit):
                    circuits[i].append(closest_pair[1])
                    added = True
                if check_presence(closest_pair[1], circuit):
                    circuits[i].append(closest_pair[0])
                    added = True
            if not added:
                circuits.append([closest_pair[0], closest_pair[1]])
    circuits = clean_circuits(circuits)
    
    result = 1
    for lst in circuits[:3]:
        result *= len(lst)
    
    print(result)