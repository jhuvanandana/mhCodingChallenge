#!/usr/bin/env python
"""
Created on Tue Jun  5 17:08:32 2018

@author: Jacqueline Huvanandana
Python v3.5

"""

def is_subseq(sequence1,sequence2):
    # checks if sequence 1 is completely contained by sequence 2
    for e in sequence1:
        if e not in sequence2:
            return False
    return True

class Node:
    """Node definition for Python 3"""
    def __init__(self):
        self.word = None
        self.nodes = {} # dict of nodes
        
    def __get_all__(self):
        x = []
        for key, node in iter(self.nodes.items()): 
            if node.word:
                x.append(node.word)
            x += node.__get_all__()
        return x
    
    def __add__(self, word, iChar = 0):

        lChar = word[iChar]
        
        # if non-existent, create node
        if lChar not in self.nodes:
            self.nodes[lChar] = Node()

        # assign word if last character
        if iChar + 1 == len(word):
            self.nodes[lChar].word = word
        else:
            self.nodes[lChar].__add__(word, iChar + 1)
        return True
    
    def __get_all_with_freq__(self,k):
        # get all complete paths
        x = self.__get_all__()
        # order by desc. length
        x.sort(key=len, reverse=True)
        
        mx = x.copy()
        freqList = []
        
        while x:
            # get last pattern p
            p = x.pop()
            # compare with other patterns
            match = list(filter(lambda compP: is_subseq(p,compP),mx))
            if len(match)>k:
                freqList.append(p)
            else:
                # if infrequent, all extensions of pattern also infrequent
                x = [el for el in x if el not in match]
            
        return freqList

class prefixTree:
   def __init__(self):
       self.root = Node()
        
   def addWord(self, word):
       self.root.__add__(word)
        
   def getAll(self):
       return self.root.__get_all__()
   
   def getAllWithFreq(self,k):
       return self.root.__get_all_with_freq__(k)

if __name__ == "__main__":
    
    ## initialise tree
    pTree = prefixTree()
    
    ## add transactions from sample db
    pTree.addWord('ad')
    pTree.addWord('abd')
    pTree.addWord('cd')
    pTree.addWord('abcd')
    pTree.addWord('bc')
    pTree.addWord('d')
    pTree.addWord('bcd')
    
    ## print all complete words with frequency > k (incl. self-matches)
    k = 3
    print('MH Coding Challenge\nPrint all patterns with freq > %d'%k)
    print(pTree.getAllWithFreq(k))