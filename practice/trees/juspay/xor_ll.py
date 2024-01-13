class XORNode:
    def __init__(self, data):
        self.data = data
        self.npx = None


def XOR(a, b):
    return a ^ b if a and b else a or b


a = XORNode("a")
b = XORNode("b")
c = XORNode("c")
d = XORNode("d")


a.npx = XOR(0, id(b))
b.npx = XOR(id(a), id(c))
c.npx = XOR(id(b), id(d))
d.npx = XOR(id(c), 0)


def traverse(head):
    current = head
    prev = 0
    while current:
        print(current.data, end=" -> ")
        next_node_address = XOR(prev, current.npx)
        next_node = get_node_by_address(next_node_address)
        prev, current = id(current), next_node


def get_node_by_address(address):
    for node in [a, b, c, d]:
        if id(node) == address:
            return node


traverse(a)
