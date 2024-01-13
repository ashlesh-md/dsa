def compress(input_string):
    compressed_data = []
    prev_char = input_string[0]

    for char in input_string[1:]:
        xor_result = ord(prev_char) ^ ord(char)
        compressed_data.append(chr(xor_result))
        prev_char = char

    return "".join(compressed_data)


def decompress(compressed_string):
    decompressed_data = []
    prev_char = compressed_string[0]

    for xor_result in compressed_string[1:]:
        char = chr(ord(prev_char) ^ ord(xor_result))
        decompressed_data.append(prev_char)
        prev_char = char

    return "".join(decompressed_data)


# Example usage
input_string = "hello world"
compressed_string = compress(input_string)
decompressed_string = decompress(compressed_string)

print("Original String: ", input_string)
print("Compressed String: ", compressed_string)
print("Decompressed String: ", decompressed_string)
