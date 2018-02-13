class Tree():
   '树的实现'
   def __init__(self,ltree = 0,rtree = 0,data = 0):
        self.ltree = ltree
        self.rtree = rtree
        self.data = data
class BTree():
    '二叉树的实现'
    def __init__(self,base = 0):
        self.base = base
    def _Empty(self):
        '是否为空树'
        if self.base == 0:
            return True
        else:
            return False
    def qout(self,tree_base):
        '前序遍历:根-左-右'
        if tree_base == 0:
            return
        print (tree_base.data)
        self.qout(tree_base.ltree)
        self.qout(tree_base.rtree)
    def mout(self,tree_base):
        '中序遍历:左-根-右'
        if tree_base == 0:
            return
        self.mout(tree_base.ltree)
        print (tree_base.data)
        self.mout(tree_base.rtree)
    def hout(self,tree_base):
        '后序遍历:左-右-根'
        if tree_base == 0:
            return
        self.hout(tree_base.ltree)
        self.hout(tree_base.rtree)
        print (tree_base.data)
#test

#tree1 = Tree(data=8)
#tree2 = Tree(data=9)
#tree3 = Tree(tree1,data=6)
#tree4 = Tree(tree2,0,data=7)
#base = Tree(tree3,tree4,5)
#btree = BTree(base)
#print ('前序遍历结果:')
#btree.qout(btree.base)
#print ('中序遍历结果:')
#btree.mout(btree.base)
#print ('后序遍历结果:')
#btree.hout(btree.base)
