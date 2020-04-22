'''
move 1 character at a time to get permutations
get slices of string and find permutations of each
move the last letter throughout each index
'''

def get_permutations(string):
    if len(string) <= 1:
        return set([string])
    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_all_chars_except_last = get_permutations(all_chars_except_last)
    
    permutations = set()
    for permutation_all_chars_except_last in permutations_all_chars_except_last:
        for idx in range(len(string)):
            permutation = (
                permutation_all_chars_except_last[:idx]
                + last_char
                + permutation_all_chars_except_last[idx:]
            )
            permutations.add(permutation)
    return permutations

print(get_permutations('cats'))