class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

n = node(99)
n.left = node(98)
n.left.left = node(97)
n.left.left.left = node(33)
n.left.left.right = node(22)
n.right = node(1)

def getRightNode(n, min):
    r = n.right
    if r == None:
        return min
    if r.value < min:
        return getRightNode(r, r.value)
    else:
        return getRightNode(r, min)

def getLeftNode(n, min):
    l = n.left
    if l == None:
        return min
    if l.value < min:
        return getLeftNode(l, l.value)
    else:
        return getLeftNode(l, min)

print(getLeftNode(n, n.value))