class XORNode:
    def __init__(self, value):
        self.value = value
        self.npx = None


def xor(a, b):
    return a ^ b if a and b else a or b


def insert_end(current, value):
    new_node = XORNode(value)
    new_node.npx = xor(id(current), 0)
    current.npx = xor(current.npx, id(new_node))
    return new_node


def traverse(head):
    current = head
    prev = 0
    while current:
        print(current.value, end=" -> ")
        next_node_address = xor(prev, current.npx)
        next_node = get_node_by_address(next_node_address)
        prev, current = id(current), next_node


def compress(text, node_list):
    if not text:
        return ""

    head = XORNode(text[0])
    node_list.append(head)

    prev = 0
    current = head

    for char in text[1:]:
        new_node = insert_end(current, char)
        node_list.append(new_node)
        prev, current = id(current), new_node

    compressed_text = ""
    current = head
    prev = 0

    while current:
        compressed_text += current.value
        next_node_address = xor(prev, current.npx)
        next_node = get_node_by_address(next_node_address, node_list)
        prev, current = id(current), next_node

    return compressed_text


def decompress(compressed_text, node_list):
    if not compressed_text:
        return ""

    head = XORNode(compressed_text[0])
    node_list.append(head)

    prev = 0
    current = head

    for char in compressed_text[1:]:
        new_node = insert_end(current, char)
        node_list.append(new_node)
        prev, current = id(current), new_node

    decompressed_text = ""
    current = head
    prev = 0

    while current:
        decompressed_text += current.value
        next_node_address = xor(prev, current.npx)
        next_node = get_node_by_address(next_node_address, node_list)
        prev, current = id(current), next_node

    return decompressed_text


def get_node_by_address(address, node_list):
    for node in node_list:
        if id(node) == address:
            return node


def print_linked_list(head):
    current = head
    prev = 0
    while current:
        next_node_address = xor(prev, current.npx)
        next_node = get_node_by_address(next_node_address)
        prev, current = id(current), next_node
    print("None")


# Example usage with user input:
user_input = input("Enter a long string: ")

node_list = []
compressed_text = compress(user_input, node_list)
print("Compressed Text:", compressed_text)

decompressed_text = decompress(compressed_text, node_list)
print("Decompressed Text:", decompressed_text)
