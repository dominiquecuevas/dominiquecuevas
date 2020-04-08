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
    >>> root.is_valid_recursively()
    True

    >>> new_root = BinaryTreeNode(50)
    >>> thirty = new_root.insert_left(30)
    >>> eighty = new_root.insert_right(80)
    >>> twenty = thirty.insert_left(20)
    >>> sixty = thirty.insert_right(60)
    >>> seventy = eighty.insert_left(70)
    >>> ninety = eighty.insert_right(90)
    >>> new_root.is_valid()
    False
    >>> new_root.is_valid_recursively()
    False
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

    def is_valid_recursively(self, floor=-float('inf'), ceiling=float('inf')):
        if self.value < floor or self.value > ceiling:
            return False
        return (self.left.is_valid_recursively(floor=floor, ceiling=self.value) if self.left else True) and (
            self.right.is_valid_recursively(floor=self.value, ceiling=ceiling) if self.right else True)


if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')