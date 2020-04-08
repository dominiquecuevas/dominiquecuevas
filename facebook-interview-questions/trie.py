class Trie:
    '''    
    >>> trie = Trie()
    >>> trie.add_word('batman')
    True
    >>> trie.root_node
    {'b': {'a': {'t': {'m': {'a': {'n': {'end': {}}}}}}}}
    >>> trie.add_word('bat')
    True
    >>> trie.root_node
    {'b': {'a': {'t': {'m': {'a': {'n': {'end': {}}}}, 'end': {}}}}}
    '''

    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        for char in word:
            if not char in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if 'end' not in current_node:   # include case if 'batman' was added before 'bat', to add an end to 'bat' and is_new_word set to True
            is_new_word = True
            current_node['end'] = {}
        return is_new_word
    # space complexity O(26**n) for 26 possible characters at each level that have 26 possible characters until the end

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')