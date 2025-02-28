class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, words):
        return [w for w in words if sorted(w.lower()) == self.sorted_word and w.lower() != self.word]
