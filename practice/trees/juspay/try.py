class Node:
    def __init__(self, data):
        self.data = data
        self.ptr_xor = 0


def xor_linked_list_compress(text, key):
    compressed_data = []
    prev_address = 0

    for char in text:
        node = Node(ord(char) ^ key)
        node.ptr_xor = prev_address
        compressed_data.append(node)
        prev_address = id(node)

    return compressed_data


def xor_linked_list_decompress(compressed_data, key):
    decompressed_text = ""

    prev_node = None
    for node in compressed_data:
        current_char = chr(node.data ^ key)
        decompressed_text += current_char

        if prev_node is not None:
            prev_node.ptr_xor ^= id(node)

        prev_node = node

    return decompressed_text


# Example usage:
original_text = "Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!"
compression_key = 42

compressed_list = xor_linked_list_compress(original_text, compression_key)
decompressed_text = xor_linked_list_decompress(compressed_list, compression_key)

print("Original Text:", original_text)
print("Compressed Data:", [node.data for node in compressed_list])
print("Decompressed Text:", decompressed_text)
