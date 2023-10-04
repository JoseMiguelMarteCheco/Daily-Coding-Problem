class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_with_prefix(node, prefix)

    def _find_words_with_prefix(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)
        for char, child_node in node.children.items():
            result.extend(self._find_words_with_prefix(child_node, prefix + char))
        return result

def autocomplete(query, word_set):
    trie = Trie()
    for word in word_set:
        trie.insert(word)
    
    return trie.search_prefix(query)

# Example usage:
query_string = "de"
word_set = ["dog", "deer", "deal", "desk"]
result = autocomplete(query_string, word_set)
print(result)
