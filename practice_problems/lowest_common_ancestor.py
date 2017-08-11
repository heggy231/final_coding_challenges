"""
Lowest Common Ancestor
"""

class BSTNode(object):
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        return '<Node {}>'.format(self.value)

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root



one = BSTNode(1, None, None)
five = BSTNode(5, None, None)
eleven = BSTNode(11, None, None)
sixteen = BSTNode(16, None, None)
three = BSTNode(3, one, five)
fifteen = BSTNode(15, eleven, sixteen)
eight = BSTNode(8, three, fifteen)


def lowest_common_ancestor(root, a, b):
    """
    >>> lowest_common_ancestor(eight, three, fifteen)
    <Node 8>
    >>> lowest_common_ancestor(eight, eleven, sixteen)
    <Node 15>
    >>> lowest_common_ancestor(eight, three, one)
    <Node 3>

    """

    # if the node is the left or the right, then return the node.
    # if the node is None, return
    # Keep recursing on the left until you return
    # Keep recursing on the right until you return


    if (root == a) or (root == b):
        return root

    if root is None:
        return

    left = lowest_common_ancestor(root.left, a, b)
    right = lowest_common_ancestor(root.right, a, b)

    if left and right:
        return root

    if left and not right:
        return left
    else:
        return right

    

















