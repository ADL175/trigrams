
import pytest

# TRI_SOURCE_LIST = [
#         ["I", "wish", "I", "may"], 
#         {'I wish': ['I'], 'wish I':['may']}
#     ]


# NEW_WORD_LIST = [
#     (["I", "wish", "I"], {"I", "wish" = "I"})
#     ]

# @pytest.mark.parametrize('n, result', TRI_SOURCE_LIST)
def test_trigrams_process_src():
    from trigrams import trigrams_process_src
    assert trigrams_process_src(["I", "wish", "I", "may"]) == {'I wish': ['I'], 'wish I': ['may']}


# @pytest.mark.parametrize('src_path, int_words, result', TRI_SOURCE)
# def test_trigrams_select_new_word():
#     from trigrams import trigrams_select_new_word
#     assert trigrams_select_new_word(TRI_SOURCE[0], TRI_SOURCE[1]) ==


# @pytest.mark.parametrize('src_path, int_words, result', TRI_SOURCE)
# def test_trigrams():
#     from trigrams import trigrams
#     assert trigrams(TRI_SOURCE[0], TRI_SOURCE[1]) ==
