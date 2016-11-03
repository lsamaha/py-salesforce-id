__author__ = 'lsamaha'


def tolongid(short_id):
    """
    Break any 15 character Salesforce ID into 3 5 character strings. Reverse the characters in each.
    Convert all uppercase alpha characters to 1. Convert any other character to 0.
    Find each result in the char lookup table. Appended each to the original ID.
    Algorithm described here: \
    http://salesforce.stackexchange.com/questions/27686/how-can-i-convert-a-15-char-id-value-into-an-18-char-id-value
    :return: an 18 character salesforce ID
    """
    if short_id == None:
        return None
    elif len(short_id) == 18:
        return short_id
    elif len(short_id) != 15:
        return None
    char_codes = {
        "00000":'A', "00001": 'B', "00010": 'C', "00011": 'D', "00100": 'E',
        "00101": 'F', "00110": 'G', "00111": 'H', "01000": 'I', "01001": 'J',
        "01010": 'K', "01011": 'L', "01100": 'M', "01101": 'N', "01110": 'O',
        "01111": 'P', "10000": 'Q', "10001": 'R', "10010": 'S', "10011": 'T',
        "10100": 'U', "10101": 'V', "10110": 'W', "10111": 'X', "11000": 'Y',
        "11001": 'Z', "11010": '0', "11011": '1', "11100": '2', "11101": '3',
        "11110": '4', "11111": '5'
    }
    # break into 3
    ids = [short_id[0:5], short_id[5:10], short_id[10:15]]
    # reverse each
    ids = [id[::-1] for id in ids]
    # swap 0|1 for uppercase alpha char|others
    bin_words = []
    for w in ids:
        w2 = []
        [w2.append('1' if c.istitle() else '0') for c in w]
        bin_words.append(''.join(w2))
    sfx = []
    [sfx.append(char_codes[word]) for word in bin_words]
    return short_id + ''.join(sfx)
