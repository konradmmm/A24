import argparse
import sys
#this code takes a string as an argument and returns it as an encoded string that shows how many times a character
#repeats itself. It will tell you whether or not the compression was more efficient than the original code
#it finishes by decompressing the compressed string using a list of keys that were generated during compression



def parse_input():
    check_var =""
    parser = argparse.ArgumentParser('Create Huffman code')
    parser.add_argument('-t', '--test', type=str,required=True, help='enter a string and see if Huffman coding would be shorter')
    args, unknown = parser.parse_known_args()
    if args.test == "":
        print("You cannot enter an empty string. Aborting")
        sys.exit(1)
    else:
        return args.test

def compress_string(string):
    compressed_string = string[0]
    repeat_counter = 1
    for letters in range(len(string)):
        if letters > 0:
            if string[letters-1] == string[letters]:
                repeat_counter+=1
            else:
                compressed_string += str(repeat_counter) + "/0"
                repeat_counter = 1
                compressed_string += string[letters]
    compressed_string += str(repeat_counter) + "/0"
    print(f"\nthe string compressed is: {compressed_string}")
    return compressed_string
def decompress_string(string):
    decoded_string = ""
    indexer = ""
    pos = 0
    for search in range(len(string)):
        if string[search] == "/" and string[search+1] == "0":
            indexer = string[pos+1:search]
            decoded_string += int(indexer) * string[pos]
            pos = search+2
    return decoded_string

def compare_strings(original_string, compressed_string):
    oglen = len(original_string)
    complen = len(compressed_string)
    if complen > oglen:
        print("\nHuffman code not required")
    elif complen < oglen:
        print("\nHuffman code more efficient")
    else:
        print("\nLengths are the same no advantage of compressed or uncompressed")
    print(f"original string len: {oglen} compressed string length: {complen}")



huff_string = parse_input()
compressed_string = compress_string(huff_string)
compare_strings(huff_string, compressed_string)
print(f"Decompressed version was: {decompress_string(compressed_string)}")




