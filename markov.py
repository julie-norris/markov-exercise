"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path)
    return contents.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    for i in range(len(words)):
        # if i < len(words) - 1:
        #     j = i + 1

        pair = (words[i], words[(i+1)%len(words)])
        if not pair in chains:
            chains[pair] = []
        chains[pair].append(words[(i+2)%len(words)])

    # your code goes here
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    first_key = choice(chains.keys())
    first_choice = choice(chains[first_key])
    link = [first_key[0], first_key[1], first_choice]
    words.extend(link)

    while True:
        current_key = (words[-2], words[-1])
        new_choice = choice(chains[current_key])

        words.append(new_choice)
        if len(words) > 10 and (words[-1][-1] == '?' or words[-1][-1] == "!"):
            break
    print " ".join(words)


input_path = "green-eggs.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
