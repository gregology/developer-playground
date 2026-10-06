"""Text helpers used by scripts that summarise documents."""

import re


def slugify(title: str) -> str:
    """Return a lowercase, hyphen-separated slug for *title*."""
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).lstrip("-")


def word_count(text: str) -> int:
    """Count whitespace-separated words in *text*."""
    return len(text.split())


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the *n* most common lowercase words with their counts."""
    counts: dict[str, int] = {}
    for word in re.findall(r"[a-z']+", text.lower()):
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]


def sentence_count(text: str) -> int:
    """Count the sentences in *text*."""
    return len(re.findall(r"[.!?]+", text))
