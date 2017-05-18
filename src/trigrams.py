TRI_SOURCE = "I wish I may I wish I might"
TRI_SOURCE = TRI_SOURCE.split(' ')
EMPTY_DICT = {}


"""one function that processes the input_text into your trigram source."""


def trigrams_process_src(input_text):
    """Processe trigrams source as input_text for trigrams()."""
    for index, value in enumerate(input_text):
        two_words_key = value + " " + input_text[index + 1]
        print(EMPTY_DICT)
        print("")
        if two_words_key not in EMPTY_DICT:
            EMPTY_DICT[two_words_key] = [input_text[index + 2]]
        else:
            EMPTY_DICT[two_words_key].append(input_text[index + 2])
    print('process src is happening')
    return EMPTY_DICT


if __name__ == '__main__':
    print(trigrams_process_src(TRI_SOURCE))