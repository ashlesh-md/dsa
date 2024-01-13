class XORNode:
    def __init__(self, value):
        self.value = value
        self.npx = None  # XOR of next and previous node addresses


def xor(a, b):
    return a ^ b if a and b else a or b


def insert_end(prev, current, value):
    new_node = XORNode(value)
    new_node.npx = xor(id(current), 0)
    current.npx = xor(current.npx, id(new_node))  # Update current node's npx
    return new_node


def traverse(head):
    current = head
    prev = 0
    while current:
        print(current.value, end=" -> ")
        next_node_address = xor(prev, current.npx)
        next_node = get_node_by_address(next_node_address)
        prev, current = id(current), next_node


def get_node_by_address(address):
    for node in node_list:
        if id(node) == address:
            return node


# Example usage with user input:
node_list = []

user_input = input("Enter a long string: ")

if user_input:
    head = XORNode(user_input[0])
    node_list.append(head)

    prev = 0
    current = head

    for char in user_input[1:]:
        new_node = insert_end(prev, current, char)
        node_list.append(new_node)
        prev, current = id(current), new_node

    print("XOR-Linked List:")
    traverse(head)
else:
    print("Input string should not be empty.")
