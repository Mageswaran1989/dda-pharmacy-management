import string
from typing import Dict

d : Dict = {}



class Dictionary(object):
    def __init__(self):
        self.N = 5
        self._data = []

    def hash(self, element):
        lookup = string.ascii_lowercase
        lookup = [(c, i) for i, c in enumerate(lookup)]

