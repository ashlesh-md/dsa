import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char=None, frequency=None):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    frequency_dict = defaultdict(int)
    for char in text:
        frequency_dict[char] += 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(frequency=left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def build_huffman_codes(node, current_code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node is not None:
        if node.char is not None:
            code_dict[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", code_dict)
        build_huffman_codes(node.right, current_code + "1", code_dict)

    return code_dict


def compress(text, code_dict):
    compressed_text = "".join(code_dict[char] for char in text)
    return compressed_text


def decompress(compressed_text, root):
    current_node = root
    decompressed_text = ""

    for bit in compressed_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decompressed_text += current_node.char
            current_node = root

    return decompressed_text


# Example usage:
original_text = "abracadabra"
huffman_tree = build_huffman_tree(original_text)
huffman_codes = build_huffman_codes(huffman_tree)

compressed_text = compress(original_text, huffman_codes)
decompressed_text = decompress(compressed_text, huffman_tree)

print(f"Original Text: {original_text}")
print(f"Compressed Text: {compressed_text}")
print(f"Decompressed Text: {decompressed_text}")
