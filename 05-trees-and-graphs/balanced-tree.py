class BinaryTreeNode:
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

def is_balanced(root):
    '''
    >>> seven = BinaryTreeNode(7)
    >>> five = seven.insert_left(5)
    >>> twelve = seven.insert_right(12)
    >>> three = five.insert_left(3)
    >>> six = five.insert_right(6)
    >>> one = three.insert_left(1)
    >>> four = three.insert_right(4)
    >>> nine = twelve.insert_left(9)
    >>> fifteen = twelve.insert_right(15)
    >>> eight = nine.insert_left(8)
    >>> ten = nine.insert_right(10)
    >>> thirteen = fifteen.insert_left(13)
    >>> seventeen = fifteen.insert_right(17)
    >>> is_balanced(seven)
    True
    >>> eighteen = seventeen.insert_right(18)
    >>> nineteen = eighteen.insert_right(19)
    >>> is_balanced(seven)
    False
    '''

    stack = [(root, 0)]
    levels = []
    while stack:
        node, level = stack.pop()
        if level not in levels and not node.left and not node.right:
            levels.append(level)
            if len(levels) > 2 or (len(levels) == 2 and abs(levels[0] - levels[1]) > 1):
                return False
        if node.left:
            stack.append((node.left, level + 1))
        if node.right:
            stack.append((node.right, level + 1))
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')