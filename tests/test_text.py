from playground.text import slugify, top_words, word_count


def test_slugify_joins_words_with_hyphens():
    assert slugify("Hello World") == "hello-world"


def test_word_count_ignores_extra_whitespace():
    assert word_count("  one  two\nthree ") == 3


def test_top_words_orders_by_count_then_alphabetically():
    assert top_words("b a b c a b", n=2) == [("b", 3), ("a", 2)]
