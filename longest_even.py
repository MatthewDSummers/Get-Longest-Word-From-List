import re

"""""""""

Function: get_longest_words(input_str, options=None)

    Explanation: 
        Get the longest word(s) from the input string.

    Args:
        input_str (str): The input string.
        options (str; optional): Filter by word length. Can be one of:
            - "odd": compares odd length words only
            - "even":  compares even length words only
            - No option selected / None: Get the longest word(s) regardless of word length.

    Return type: 
        list or False. A list of longest words from the string per options; or False if conditions not met

    Notes:
        Hyphenated words are considered one word
        Compares character count of words irrespective of any capital letters

"""""""""

def get_longest_words(input_str, options=None):
    if not isinstance(input_str, str):
        print("get_longest_words() needs a string as input data")
        return False

    longest = []
    alphabet_only_string = re.sub(r'[^a-zA-Z -]', '', input_str)
    for word in alphabet_only_string.split(" "):
        word = word.lower()
        nohyphens = word.replace("-", "")

        if options == "even":
            if len(nohyphens) % 2 == 0:
                longest = prepare_longest_words_list(longest, nohyphens, word)

        elif options == "odd":
            if len(nohyphens) % 2 != 0:
                longest = prepare_longest_words_list(longest, nohyphens, word)

        elif not options:
            longest = prepare_longest_words_list(longest, nohyphens, word)

    if not longest:
        print("No even letter words found")
        return False

    return longest


def prepare_longest_words_list(longest, nohyphens, word):
    if longest == [] or len(nohyphens) > len(longest[0].replace("-", "")):
        return [word]
    elif len(nohyphens) == len(longest[0].replace("-", "")):
        if word not in longest:
            longest.append(word)
    return longest


print(get_longest_words([2,2,2]))
# Output: 
    # Prints: get_longest_words needs() a string as input data
    # Returns: False

print(get_longest_words("Hyphenated-word is 14 letters (not counting the hyphen). nanotechnology is also 14 letters. 'hyphenated-word' appears twice", "even"))
# Output: ['hyphenated-word', 'nanotechnology']

print(get_longest_words("hyphenated-word is 14 (not counting the hyphen). prestidigitation is 16 letters", "even"))
# Output: ['prestidigitation']

print(get_longest_words("The quick brown dog jumps", "odd"))
# Output: ['quick', 'brown', 'jumps']

print(get_longest_words("The quick brown dog jumps", "even"))
# Output: 
    # Prints: No even letter words found
    # Returns: False

print(get_longest_words("Neither odd nor even; let's just get the longest words"))
# Output: ['neither', 'longest']