# from abc import ABC
from collections import deque
from collections.abc import MutableMapping
from typing import Optional, List


class MapInterface(MutableMapping):
    class Node(object):
        __slots__ = 'left', 'right', 'word', 'meaning'

        def __init__(self, word: str, meaning: str):
            self.left = None
            self.right = None
            self.word = word
            self.meaning = meaning

        def __str__(self):
            return str(self.meaning)


class BSTMap(MapInterface):
    def __init__(self):
        self.root = None
        self._length = 0
        self.treenodes = []
        self.sub_string_results = []

    def add(self, root, node: MapInterface.Node):
        if root is not None:
            if node.word <= root.word:
                if root.left:
                    self.add(root.left, node)
                else:
                    root.left = node
            elif node.word > root.word:
                if root.right:
                    self.add(root.right, node)
                else:
                    root.right = node

    def insert(self, node: MapInterface.Node):
        if self.root is None:
            self.root = node
        else:
            self.add(self.root, node)

    def search(self, root: MapInterface.Node, word: str):
        if root is None:
            return False
        elif word == root.word or root.word.startswith(word):
            return root.meaning
        elif word < root.word:
            return self.search(root.left, word)
        else:
            return self.search(root.right, word)

    def find(self, word: str):
        return self.search(self.root, word)

    # def sub_string(self, node: MapInterface.Node, data):
    #     if node is not None:
    #         self.sub_string(node.left, data)
    #         if data in node.word:
    #             self.sub_string_results.append(node.word)
    #         self.sub_string(node.right, data)

    def find_sub_string(self, sub_string: str):
        # self.sub_string_results = []
        # self.sub_string(self.root, prefix)
        ret = []
        for k, v in self.items():
            if sub_string in k:
                ret.append(k)
        return ret

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.treenodes.append(node.word)
            self.inorder(node.right)

    def __str__(self):
        self.inorder(self.root)
        return ""

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        return self.find(k)

    def __setitem__(self, k, v):
        node = MapInterface.Node(word=k, meaning=v)
        self.insert(node=node)
        self._length += 1

    def __delitem__(self, k):
        pass

    def __iter__(self):
        self.inorder(self.root)
        return iter(self.treenodes)


def split_line(line):
    word, meaning = line.split("/")
    return word.strip(), meaning.strip()


def get_input_data():
    with open("InputPS12Q1.txt") as f:
        input_data = f.readlines()
        input_data = list(map(lambda line: split_line(line), input_data))
    return input_data


def split_line_prompts(line):
    category, word = line.split(":")
    return category.strip(), word.strip()


def get_prompts():
    strings = []
    sub_strings = []
    with open("PromptsPS12Q1.txt") as f:
        input_data = f.readlines()
        for line in input_data:
            category, word = split_line_prompts(line)
            if category == "SearchWord":
                strings.append(word)
            else:
                sub_strings.append(word)
    return strings, sub_strings

def get_results():
    ret = []
    input_data = get_input_data()

    bst_dict = BSTMap()

    ret.append("-----------Reading from file ArraydictPS12.txt -------------")
    for word, meaning in input_data:
        bst_dict[word] = meaning
    ret.append(f"BST Created with {len(bst_dict)} nodes")

    ret.append("---------------------------------------------------")

    strings, sub_strings = get_prompts()

    ret.append("---------------- Search words ------------------------")

    for s in strings:
        res = bst_dict.find(s)
        if res is False:
            ret.append(f"{s}" + " - " + "not found")
        else:
            ret.append(f"{s}" + " - " + f"{res}")

    ret.append("---------------------------------------------------")

    for sub_str in sub_strings:
        ret.append(f"---------------- Sub String: {sub_str} ------------------------")
        sub_string_results = bst_dict.find_sub_string(sub_str)
        for r in sub_string_results:
            ret.append(r)
        ret.append("---------------------------------------------------")

    # for k,v in bst_dict.items():
    #     print(k, v)
    return ret


if __name__ == '__main__':
    res = get_results()
    for line in res:
        print(line)
    # with open("OutputPS12Q1.txt", "w") as f:
    #     for line in res:
    #         f.write(line)
    #         f.write("\n")


