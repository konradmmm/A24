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
    key_list = [0]
    key_counter = 0
    repeat_counter = 1
    for letters in range(len(string)):
        if letters > 0:
            if string[letters-1] == string[letters]:
                repeat_counter += 1
            else:
                compressed_string += str(repeat_counter)
                key_list.append(len(str(repeat_counter)) + key_list[key_counter]+1)
                key_counter += 1
                repeat_counter = 1
                compressed_string += string[letters]
    compressed_string += str(repeat_counter)
    key_list.append(len(str(repeat_counter)) + key_list[key_counter] + 1)
    print(f"compressed string: {compressed_string}")
    return compressed_string, key_list
def compare_strings(original_string, compressed_string):
    oglen = len(original_string)
    complen = len(compressed_string)
    if complen > oglen:
        print("\nHuffman code not required")
        print(f"original string len: {oglen} compressed string length: {complen}")
    elif complen < oglen:
        print("\nHuffman code more efficient")
        print(f"original string len: {oglen} compressed string length: {complen}")
    else:
        print("\nLengths are the same no advantage of compressed or uncompressed")
        print(f"original string len: {oglen} compressed string length: {complen}")
def decompress_string(encoded_string, key_list):
    key_index = 1
    decoded_string = ""
    indexer = ""
    for amount in key_list[:-1]:
        indexer =  encoded_string[amount+1:key_list[key_index]]
        if key_index != len(key_list)-1:
            key_index += 1
        character = encoded_string[amount]
        decoded_string += int(indexer) * character
    print(decoded_string)


huff_string = parse_input()
compressed_string, keys = compress_string(huff_string)
compare_strings(huff_string, compressed_string)
decompress_string(compressed_string,keys)





