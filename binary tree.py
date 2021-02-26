def binary_tree(root):
    return [root, [], []]


def addLeftBranch(root, branch):
    t = root.pop(1)
    if len(branch) >= 1:
        root.insert(1, branch)
    else:
        root.insert(1,["branch", [], []])


def addRightBranch(root, branch):
    t = root.pop(2)
    if len(branch) >= 1:
        root.insert(2, branch)
    else:
        root.insert(2, ['branchRight',[],[]])


def getRightChildOf(tree):
    return(tree[2])


def getLeftChildOf(tree):
    return(tree[1])


root = binary_tree("root")
subTreeLeftOne = ['branchLeft', ["i'm the left leaf"], ["I'm the right leaf"]]
subTreeRightOne = ['branchRight', [f"i'm the left leaf..."], []]

#print(root, "\n")

addLeftBranch(root, subTreeLeftOne) 

#print(root, "\n")


addRightBranch(root, subTreeRightOne)

#print(root)

branchLeft_child = ["Hey, i'm a child of branch left", [], []]

addLeftBranch(root[1], branchLeft_child)

#print(root)


#print(getRightChildOf(getLeftChildOf(root)))


root = binary_tree('a')
addLeftBranch(root, binary_tree('b')) # primer nivel izquierdo
addRightBranch(root, binary_tree('c'))# primer nivel derecho

addRightBranch(getLeftChildOf(root), binary_tree('d')) #Segundo nivel, hijo de left subtree

#Segundo nivel, hijos de right subtree
addRightBranch(getRightChildOf(root), binary_tree('f'))
addLeftBranch(getRightChildOf(root), binary_tree('e'))



counter = 0
def printBranches(counter, tree):
    counter = counter
    print((" " * counter) + "+" + ("-" * counter), tree[0], sep = "") # sería el primer elemento(root de cada tree/subTree)
    rightSubTree = getRightChildOf(tree)
    leftSubTree = getLeftChildOf(tree)
    if len(rightSubTree) != 0:
        printBranches(counter + 1, getRightChildOf(tree))
    else: pass
    if len(leftSubTree) != 0:
        printBranches(counter + 1, getLeftChildOf(tree))
    else: pass
printBranches(counter, root)



###############################
# POO class BtnaryTree Aproach-
###############################


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        self.father = None
        

    def insert_left(self, new_Node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(new_Node)
            
            self.leftChild.father = self.key # Nombre del nodo padre
            
        else:
            t = BinaryTree(new_Node)
            t.father = self.leftChild.father # el padre de t será el del nodo desplazado
            self.leftChild.father = t.key # el padre del nodo desplzado es t
            t.leftChild = self.leftChild
            self.leftChild = t


    def insert_Right(self, new_Node):
        if self.RightChild == None:
            self.RightChild = BinaryTree(new_Node)

            self.rightChild.father(key) # Nombre del nodo padre

        else:
            t = BinaryTree(new_Node)
            t.father = self.rightChild.father # el padre de t será el del nodo desplazado
            self.rightChild.father = t # el padre del nodo desplzado es t
            t.RightChild = self.RightChild
            self.leftChild = t


    def father(self):
        return self.father


    def get_right_child(self):
        return self.rightChild


    def get_left_child(self):
        return self.leftChild
    

    def set_root_val(self, obj):
        self.key = obj


    def get_root_val(self):
        return self.key

















