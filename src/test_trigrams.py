
import pytest

TRI_SOURCE_LIST = [
    ('One night--it', ['was']),
    ('night--it was', ['on']),
    ('was on', ['the']),
    ('on the', ['twentieth']),
    ('the twentieth', ['of'])
]


# dirpath = os.path.dirname(os.path.abstpath(__file__))
# source_file = os.path.join(dirpath, 'body_text.txt')

# import pdb; pdb.set_trace()

@pytest.mark.parametrize('n, result', TRI_SOURCE_LIST)
def test_trigrams_build_dict(n, result):
    from trigrams import trigrams_build_dict
    assert trigrams_build_dict()[n] == result


def test_trigrams_random_int():
    from trigrams import trigrams_random_int
    for n in range(1, 100):
        assert trigrams_random_int(n) in range(n)
