class BinaryTreeNode(object):
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

    >>> new_root = BinaryTreeNode(50)
    >>> thirty = new_root.insert_left(30)
    >>> eighty = new_root.insert_right(80)
    >>> twenty = thirty.insert_left(20)
    >>> sixty = thirty.insert_right(60)
    >>> seventy = eighty.insert_left(70)
    >>> ninety = eighty.insert_right(90)
    >>> new_root.is_valid()
    False

    >>> root = BinaryTreeNode(4)
    >>> two = root.insert_left(2)
    >>> root.left.value
    2
    >>> five = root.insert_right(5)
    >>> one = two.insert_left(1)
    >>> three = two.insert_right(3)
    >>> six = five.insert_right(6)
    >>> root.is_valid_recursively()
    True

    invalid at sixty
    >>> new_root = BinaryTreeNode(50)
    >>> thirty = new_root.insert_left(30)
    >>> eighty = new_root.insert_right(80)
    >>> twenty = thirty.insert_left(20)
    >>> sixty = thirty.insert_right(60)
    >>> seventy = eighty.insert_left(70)
    >>> ninety = eighty.insert_right(90)
    >>> new_root.is_valid_recursively()
    False
    '''
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

    def is_valid(self):
        seen = [(self, -float('inf'), float('inf'))]

        while seen:
            current, floor, ceiling = seen.pop()
            if current.value > floor and current.value < ceiling:
                if current.left:
                    seen.append((current.left, floor, current.value))
                if current.right:
                    seen.append((current.right, current.value, ceiling))
            else:
                return False
        return True

    def is_valid_recursively(self, floor=-float('inf'), ceiling=float('inf')):
        # print('self.value:', self.value)
        # print('floor:', floor)
        # print('ceiling:', ceiling)
        # print()
        if self.value < floor or self.value > ceiling:
            return False
        return (self.left.is_valid_recursively(floor=floor, ceiling=self.value) if self.left else True) and (
            self.right.is_valid_recursively(floor=self.value, ceiling=ceiling) if self.right else True)

def is_valid_recursively(root, floor=-float('inf'), ceiling=float('inf')):
    '''
    >>> root = BinaryTreeNode(4)
    >>> two = root.insert_left(2)
    >>> five = root.insert_right(5)
    >>> one = two.insert_left(1)
    >>> three = two.insert_right(3)
    >>> six = five.insert_right(6)
    >>> is_valid_recursively(root)
    True

    invalid at sixty
    >>> new_root = BinaryTreeNode(50)
    >>> thirty = new_root.insert_left(30)
    >>> eighty = new_root.insert_right(80)
    >>> twenty = thirty.insert_left(20)
    >>> sixty = thirty.insert_right(60)
    >>> seventy = eighty.insert_left(70)
    >>> ninety = eighty.insert_right(90)
    >>> is_valid_recursively(new_root)
    False
    '''
    if not root:
        return True
    if root.value < floor or root.value > ceiling:
        return False
    return is_valid_recursively(root.left, floor=floor, ceiling=root.value) and (
        is_valid_recursively(root.right, floor=root.value, ceiling=ceiling)
    )
        

'''
get the current note starting at root
get the left and right
check if left is less than parent
    check if left is less than parent
    check if left's right is greater than parent and less than grandparent
check if right is greater than parent
    check if right's left is less than parent and greater than grandparent
    check if right's right is greater than parent
'''

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('ALL TESTS PASSED')