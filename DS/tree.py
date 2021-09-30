class BinaryTree:
    lengths = []
    sumatory = 0

    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None
        self.Lengths = []

    def addLeft(self, left):
        self.left_child = BinaryTree(left)

    def addRight(self, right):
        self.right_child = BinaryTree(right)

    """
    def getLeftInstances(self):
        print(self.root)
        try:
            return self.left_child.getLeftInstances()
        except:
            return None
    """

    def printNodes(self):
        print(self.root)
        if self.right_child != None:
            self.right_child.printNodes()
        if self.left_child != None:
            self.left_child.printNodes()

    def advanceThrowTree(self, length=0):
        if self.right_child != None:
            self.right_child.advanceThrowTree(length + 1)
        if self.left_child != None:
            self.left_child.advanceThrowTree(length + 1)
        elif self.right_child == None:
            BinaryTree.lengths.append(length)

    def sumatoryNodes(self):
        BinaryTree.sumatory += self.root
        if self.right_child != None:
            self.right_child.sumatoryNodes()
        if self.left_child != None:
            self.left_child.sumatoryNodes()

    def getSumatoryNodes(self):
        self.sumatoryNodes()
        treeSum = BinaryTree.sumatory
        BinaryTree.sumatory = 0
        return treeSum
    """
    def getTreeLength(self):
        if BinaryTree.lengths == []:
            self.advanceThrowTree()
            return(max(BinaryTree.lengths))
        else:
            return(max(BinaryTree.lengths))
    """

    def getTreeLength(self):
        self.advanceThrowTree()
        treeLength = max(BinaryTree.lengths)
        BinaryTree.lengths = []
        return treeLength


root = BinaryTree("root")

root.addRight("R")
root.right_child.addRight("RR")
root.right_child.addLeft("RL")
root.right_child.right_child.addRight("RRR")

root.addLeft("L")
root.left_child.addLeft("LL")
root.left_child.addRight("LR")
root.left_child.right_child.addLeft("LRL")
root.left_child.right_child.left_child.addRight("LRLR")

# print(root.getTreeLength())

ScrumMasta = BinaryTree("Fernan")
ScrumMasta.addRight("Rodro")
ScrumMasta.addLeft("Teo")
ScrumMasta.left_child.addRight("CJ")

# print(ScrumMasta.getTreeLength())
# ScrumMasta.printNodes()

numTree = BinaryTree(1)
numTree.addLeft(2)
numTree.addRight(3)
numTree.left_child.addLeft(4)
numTree.left_child.addRight(5)
numTree.right_child.addLeft(6)
numTree.right_child.addRight(7)

print(numTree.getSumatoryNodes())
