import argparse

def parse_input():
    parser = argparse.ArgumentParser('Create Huffman code')
    parser.add_argument('-t', '--test', required=True, type=str,
                        help='enter a string and see if Huffman coding would be shorter')
    args, unknown = parser.parse_known_args()
    return args.test

def compress_string(string):
    compressed_string = string [0]
    counter = 1
    for letters in range(len(string)):
        if letters > 0:
            if string[letters-1] == string[letters]:
                counter += 1
            else:
                compressed_string += str(counter)
                counter = 1
                compressed_string += string[letters]
    compressed_string += str(counter)
    print(f"Orginal string: {string}")
    print(f"compressed string: {compressed_string}")
    return compressed_string
def compare_strings(original_string, compressed_string):
    if len(compressed_string) > len(original_string):
        print("Huffman code not required")
    elif len(compressed_string) < len(original_string):
        print("Huffman code more efficient")
    else:
        print("Lengths are the same no advantage of compressed or uncompressed")


Huff_string = parse_input()
compressed_string = compress_string(Huff_string)
compare_strings(Huff_string, compressed_string)


