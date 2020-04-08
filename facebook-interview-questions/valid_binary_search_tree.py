class BinaryTreeNode:
    '''
    >>> root = BinaryTreeNode(4)
    >>> two = root.insert_left(2)
    >>> root.left.value
    2
    >>> five = root.insert_right(5)
    >>> one = two.insert_left(1)
    >>> three = two.insert_right(3)
    >>> six = five.insert_right(6)
    >>> root.is_valid()
    True
    '''

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left
    
    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_valid(self):
        seen = [(self, -float('inf'), float('inf'))]

        while seen:
            node, floor, ceiling = seen.pop()

            if node.value < floor or node.value > ceiling:
                return False
            if node.left:
                seen.append((node.left, floor, node.value))
            if node.right:
                seen.append((node.right, node.value, ceiling))
        return True
    
    # time complexity O(n)
    # space complexity O(n)
    # depth first search with stack

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')