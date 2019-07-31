class CorrelationMap:
    wordHash = {}
    def addWord(self, wordNode):
        self.wordHash[wordNode.name] = wordNode
class WordNode:
    def __init__(self, name):
        self.name = name
class WordStockConnection:
    def __init__(self, word, stock):
        self.word = word
        self.stock = stock
