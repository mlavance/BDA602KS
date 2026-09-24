import re

import pandas as pd


class Data_class:
    """
    takes unprocessed data from plaintext and adds various 
    categorical facts derived from the plaintext of them
    """
    
    def __init__(self, data: pd.DataFrame, words: list | None = None):
        """
        data must be passed as dataframe with contents labeled "Message"
        """
        self.data = data
        
        self.data["word_count"] = self.data["Message"].str.split().str.len()
        if words != None:
            for i in words:
                self._determine_word_freq(i)

    def _get_all(self):
        return 1

    def _determine_word_freq(self, word: str, case_sensitive: bool = False):
        pattern = rf"\b{re.escape(word)}\b"
        flags = 0 if case_sensitive else re.IGNORECASE

        counts = self.data["Message"].str.count(pattern, flags=flags)
        self.data[f"word_freq_{word}"] = counts / self.data["word_count"].replace(0, pd.NA)
        return 1




