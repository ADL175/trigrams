import random
import io
import os
import sys


def main(input_body = 'body_text.txt', n = "21"):
    if os.path.isfile(input_body):
        if os.stat(input_body).st_size >= 1:
            tri_dictionary = trigrams_build_dict(input_body)
            n = int(n)
            return trigrams_build_trigram(n, tri_dictionary)
        elif os.stat(input_body).st_size == 0:
            return 'Bro, give me more words'
    else:
        return 'Enter actual .txt file Dude'


def trigrams_build_dict(input_body = 'body_text.txt'):
    tri_dictionary = {}
    word_1 = ''
    word_2 = ''
    all_words_key = ''
    converted_unicode_text = io.open(input_body, encoding='utf-8')
    for text in converted_unicode_text:
        for word in text.split():
            if word_1 == '':
                word_1 == word
            elif word_2 == '':
                word_2 == word
            else:
                all_words_key = word_1 + ' ' + word_2
                if all_words_key in tri_dictionary:
                    list_word_3 = tri_dictionary[all_words_key]
                    list_word_3.append(word)
                    tri_dictionary[all_words_key] = list_word_3
                else:
                    tri_dictionary[all_words_key] = [word]
                word_1 = word_2
                word_2 = word
    return tri_dictionary


def trigrams_random_int(x):
    from random import randint
    return randint(0, x - 1)


def trigrams_build_trigram(n, tri_dictionary):
    rand_dict_keys = random.choice(list(tri_dictionary.keys()))
    split_dict_keys = rand_dict_keys.split()
    word_1 = split_dict_keys[0]
    word_2 = split_dict_keys[1]
    generated_result = split_dict_keys[0].capitalize()
    generated_result = generated_result + ' ' + word_2
    for index in range(0, n - 2):
        all_words_key = word_1 + ' ' + word_2
        value_on_all_words_key = list(tri_dictionary[all_words_key])
        random_int = trigrams_random_int(len(value_on_all_words_key))
        new_random_word_3 = value_on_all_words_key[random_int]
        generated_result = generated_result + ' ' + new_random_word_3
        word_1 = word_2
        word_2 = new_random_word_3
        check_if_new_key_word_in_dict = word_1 + ' ' + word_2
        if check_if_new_key_word_in_dict not in tri_dictionary:
            rand_dict_keys = random.choice(list(tri_dictionary.keys()))
            split_dict_keys = rand_dict_keys.split()
            word_1 = split_dict_keys[0]
            word_2 = split_dict_keys[1]
    return generated_result


if __name__ == '__main__':
    if (len(sys.argv) == 3):
        print(main(sys.argv[1], sys.argv[2]))
    else:
        print(main())
