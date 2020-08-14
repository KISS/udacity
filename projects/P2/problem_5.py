#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[66]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = dict()  
        self.is_complete_word = False 
    
    def insert(self, char):
        ## Add a child node in this Trie
        new_node = TrieNode(char)
        self.children[new_node]

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        curr = self.root 

        for char in word:
            # if char isn't present, add it to our Trie as a child node 
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # update curr to corresponding value for char 
            curr = curr.children[char]

        # word is fully added so set the last chars `is_complete_word` property to True 
        curr.is_complete_word = True 

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return
            curr = curr.children[char]

        return curr


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[67]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = dict()  
        self.is_complete_word = False 
    
    def insert(self, char):
        ## Add a child node in this Trie
        new_node = TrieNode(char)
        self.children[new_node]
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = list()
        new_suffix = suffix
        
        # iterate through all child nodes for our current parent node
        for char, val in self.children.items():
            # node references the TrieNode properties of our current char 
            node = val
            # add char to our suffix since it'll be the "prefix" of its child nodes
            new_suffix += char

            # if current key-value pair in dict() is a complete word,
            # add it to our suffixes array 
            if node.is_complete_word:
                suffixes.append(new_suffix)
            
            # recursively add word endings to the suffixes array by calling 
            # the suffixes method on our current child node
            suffixes += node.suffixes(new_suffix)
            
            # reset new_suffix  
            new_suffix = suffix

        return suffixes


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[68]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
print(MyTrie.root.children)


# In[69]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='')


# In[ ]:




