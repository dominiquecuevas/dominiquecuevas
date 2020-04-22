def get_permutations(string):
    '''
    cats
        cat
            ca
                {c} <-len of string is 1, return the set
            {ca, ac}
        {tca, cta, cat, tac, atc, act}
    {stca, tsca, tcsa, tcas,
    scta, csta, ctsa, ctas,
    scat, csat, cast, cats,
    stac, tsac, tasc, tacs,
    satc, astc, atsc, atcs,
    sact, asct, acst, acts}
    '''
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
