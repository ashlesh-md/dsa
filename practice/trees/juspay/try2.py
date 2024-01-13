import zlib

# Example usage:
original_text = "Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!Hello, world!"

# Compression
compressed_data = zlib.compress(original_text.encode("utf-8"))

# Decompression
decompressed_text = zlib.decompress(compressed_data).decode("utf-8")

print("Original Text:", original_text)
print("Compressed Data:", compressed_data)
print("Decompressed Text:", decompressed_text)
