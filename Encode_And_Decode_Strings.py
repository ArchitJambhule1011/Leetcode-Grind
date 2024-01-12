""" 
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

"""

def encode(strs : list[str]):
    encoded_dict = {}
    for i, j in enumerate(strs):
        encoded_dict[j] = str(i)

    encoded = ''.join(encoded_dict.values())
    return encoded , encoded_dict

def decode(encoded : str, encoded_dict):
    decoded = list(encoded)
    reverse_mapping = {v: k for k, v in encoded_dict.items()}
    decoded_keys = [reverse_mapping[val] for val in decoded]

    return decoded_keys
