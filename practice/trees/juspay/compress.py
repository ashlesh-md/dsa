def compress(input_string):
    compressed_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_string += input_string[i - 1] + str(count)
            count = 1

    compressed_string += input_string[-1] + str(count)
    return compressed_string


def decompress(compressed_string):
    decompressed_string = ""
    i = 0

    while i < len(compressed_string):
        char = compressed_string[i]
        count = int(compressed_string[i + 1])
        decompressed_string += char * count
        i += 2

    return decompressed_string


# Example usage:
original_text = "aaabbbbcc"
compressed_text = compress(original_text)
decompressed_text = decompress(compressed_text)

print(f"Original Text: {original_text}")
print(f"Compressed Text: {compressed_text}")
print(f"Decompressed Text: {decompressed_text}")
