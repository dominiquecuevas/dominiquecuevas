class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

'''
go right if has a right attr, copy value of previous Node
if current has a left, reassign value and return it
else go left and reassign value to current and return
'''

def find_largest(node):
    if node.right:
        return find_largest(node.right)
    return node.value

def second_largest(node):
    '''
    >>> root = BinaryTreeNode(5)
    >>> ten = root.insert_right(10)
    >>> seven = ten.insert_left(7)
    >>> eight = seven.insert_right(8)
    >>> six = seven.insert_left(6)
    >>> find_largest(root)
    10
    >>> second_largest(root)
    8
    
                   5
                        10
                      7    
                    6   8

    >>> root = BinaryTreeNode(5)
    >>> three = root.insert_left(3)
    >>> two = three.insert_left(2)
    >>> four = three.insert_right(4)
    >>> find_largest(root)
    5
    >>> second_largest(root)
    4

                5
        3
    2       4
    '''
    if node.left and not node.right:
        return find_largest(node.left)
    if node.right and not node.right.left and not node.right.right:
        return node.value
    return second_largest(node.right)
    
    # time complexity is O(h) and space is O(h)
    # cut down to O(n) space if didn't use recursion

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('ALL TESTS PASSED')