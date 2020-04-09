class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add_next(self, value):
        self.next = LinkedListNode(value)
        return self.next

def contains_cycle(node):
    '''
    >>> node = LinkedListNode(1)
    >>> two = node.add_next(2)
    >>> three = two.add_next(3)
    >>> four = three.add_next(4)
    >>> contains_cycle(node)
    False
    >>> new_node = LinkedListNode(10)
    >>> eleven = new_node.add_next(11)
    >>> twelve = eleven.add_next(12)
    >>> twelve.next = eleven
    >>> contains_cycle(new_node)
    True
    '''
    seen = set()
    while node:
        if node in seen:
            return True
        seen.add(node)
        node = node.next
    return False
    # time complexity O(n)
    # space complexity O(n)

def contains_cycle_runners(node):
    '''
    >>> node = LinkedListNode(1)
    >>> two = node.add_next(2)
    >>> three = two.add_next(3)
    >>> four = three.add_next(4)
    >>> contains_cycle_runners(node)
    False
    >>> new_node = LinkedListNode(10)
    >>> eleven = new_node.add_next(11)
    >>> twelve = eleven.add_next(12)
    >>> twelve.next = eleven
    >>> contains_cycle_runners(new_node)
    True
    '''

    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast is slow:
            return True
    return False
    # time complexity O(n)
    # space complexity O(1)

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')