import re

import pandas as pd

from chars import chars_to_check
from strings import words_to_check


class Data_class:
    """
    takes unprocessed data from plaintext and adds various
    categorical facts derived from the plaintext of them
    """

    def __init__(self, data: pd.DataFrame, words: list | None = None, chars: list | None = None):
        """
        data must be passed as dataframe with contents labeled "Message"
        """
        self.data = data

        self.data["word_count"] = self.data["Message"].str.split().str.len()
        self.checked_words = []
        self.checked_chars = []

        self._get_all_words(words_to_check)
        if words != None:
            self._get_all_words(words)
        self._get_all_chars(chars_to_check)
        if chars != None:
            self._get_all_chars(chars)

    def _get_all_words(self, words):
        for i in words:
            self._determine_word_freq(i)
        return 1

    def _get_all_chars(self, chars):
        for i in chars:
            self._determine_char_freq(i)
        return 1

    def _determine_word_freq(self, word: str, case_sensitive: bool = False):
        pattern = rf"\b{re.escape(word)}\b"
        flags = 0 if case_sensitive else re.IGNORECASE

        counts = self.data["Message"].str.count(pattern, flags=flags)
        self.data[f"word_freq_{word}"] = (
            100 * counts / self.data["word_count"].replace(0, pd.NA)
        )
        self.checked_words.append(word)
        return 1

    def _determine_char_freq(self, char: str, case_sensitive: bool = False):
        if len(char) != 1:
            raise ValueError(f"char must be a single character, got {char!r}")

        messages = self.data["Message"]
        if not case_sensitive:
            messages = messages.str.lower()
            char = char.lower()

        counts = messages.str.count(re.escape(char))
        total = self.data["Message"].str.len().replace(0, pd.NA)

        self.data[f"char_freq_{char}"] = 100 * counts / total
        return 1
