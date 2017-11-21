from street import *
MAX_KEY_SIZE = 7

# Python code to delete a node in AVL tree
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.streets = []

    def insertData(self, street):
        self.streets.append(street)
    
    def getStreets(self):
        return self.streets
 
# AVL tree class which supports insertion,
# deletion operations
class AVL_Tree(object):
    text = []

    def __init__(self, key_size):
        self.key_size = key_size
        
    def insert(self, root, street):
        insert_key = int(street.getZipCode()/(10**(MAX_KEY_SIZE - self.key_size)))

        # Step 1 - Perform normal BST
        if not root:
            node = TreeNode(insert_key)
            node.insertData(street)
            return node
        elif insert_key < root.val:
            root.left = self.insert(root.left, street)
        elif insert_key > root.val:
            root.right = self.insert(root.right, street)
        else:
            if(street not in root.getStreets()):
                root.insertData(street)
                return root
            else:
                print("Valor já inserido")
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and insert_key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and insert_key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and insert_key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and insert_key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, code):
        delete_key = int(code/(10**(MAX_KEY_SIZE - self.key_size)))

        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif delete_key < root.val:
            root.left = self.delete(root.left, code)
 
        elif delete_key > root.val:
            root.right = self.delete(root.right, code)
        else:
            streets = root.getStreets()
            for s in streets:
                if s.getZipCode() == code:
                    root.getStreets().remove(s)
            if len(streets) == 0:
                #delete the node if its content is empty
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
    
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
    
                temp = self.getMinValueNode(root.right)
                root.val = temp.val
                root.right = self.delete(root.right,
                                        temp.val)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="\n")
        for i in root.getStreets():
            print("   " + str(i.getZipCode()))
        self.preOrder(root.left)
        self.preOrder(root.right)

    def mountFile(self, root):
        if not root:
            return
 
        self.text.append(str(root.val) + "-")
        i = 0
        while i < len(root.getStreets()):
            self.text.append(str(root.getStreets()[i].getZipCode()))
            self.text.append(";"+str(root.getStreets()[i].getName()))
            self.text.append(";"+str(root.getStreets()[i].getNbhd()))
            if (i < len(root.getStreets()) - 1):
                self.text.append(",")
            i+=1
        self.text.append("\n")
        self.mountFile(root.left)
        self.mountFile(root.right)
        
    def saveFile(self):
        file = open("tree.txt", "w")
        file.writelines(self.text)
        self.text = []

    def rebuildTree(self, filename):
        file = open(filename, "r")
        nodes = file.readlines();
        streets = []
        entrys = []
        for n in nodes:
            entrys.append(n.split("-")[1])
        sub_entries = []
        for e in entrys:
            sub_entries.append(e.split(","))
        
        for sub in sub_entries:
            for i in sub:
                streets.append(Street(int(i.split(";")[0]), i.split(";")[1], i.split(";")[2]))
        
        return streets

    def search(self, root, code):
        seach_key = int(code/(10**(MAX_KEY_SIZE - self.key_size)))

        if not root:
            return None
        elif seach_key < root.val:
            root.left = self.search(root.left, code)
        elif seach_key > root.val:
            root.right = self.search(root.right, code)
        else:
            for s in root.getStreets():
                if(s.getZipCode() == code):
                    return s
            return None
    