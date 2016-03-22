import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from binary_search_tree import Tree

#from .binary_search_tree import Tree


bst = Tree()
bst.insert(10)
print(bst.insert(15))
bst.preorder()
bst.postorder()
bst.inorder()