##

### Design add and search words data structure

## Design a data structure that supports adding new words and finding if a string matches any previously added string.

### Implement the WordDictionary class:

# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# ## Example:
#
# ### Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#
# ### Output
# [null,null,null,null,false,true,true,true]
#
# ## Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

from typing import Any, List, Dict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        for i, ch in enumerate(word):
            if ch == '.':
                for child in node.children.values():
                    if self._search_in_node(word[i+1:], child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                node = node.children[ch]
        return node.is_end_of_word


word_dict = WordDictionary()
word_dict.addWord("bad")
word_dict.addWord("dad")
word_dict.addWord("mad")

print(f"search for '': {word_dict.search('')}")
print(f"search for pad: {word_dict.search('pad')}")
print(f"search for bad: {word_dict.search('bad')}")
print(f"search for ba: {word_dict.search('ba')}")
print(f"search for bac: {word_dict.search('bac')}")
print(f"search for .ad: {word_dict.search('.ad')}")
print(f"search for b..: {word_dict.search('b..')}")
print(f"search for b.c: {word_dict.search('b.c')}")

