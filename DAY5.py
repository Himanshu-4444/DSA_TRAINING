#Tree
'''Tree is a non-linear data structure that organizes data hierarchically. It consists of nodes connected by edges, 
with a single root node at the top and child nodes branching out below it. Each node can have zero or more child nodes, 
and nodes without children are called leaf nodes. Trees are widely used in computer science for various applications, 
including representing hierarchical relationships between its elements, without having any cycle, it is basically reversed a real life tree.
quicker and easier access to data
store hierarchical data,like folder structure,organizational structure, etc, html/xml data, etc
there are many diffrent types of data strutures which performs better in various situations 
binary search tree,avl, red black tree, trie.
root: top node without parent
edge: a link between parent and child
leaf a node which does not have child
sibling: children of same parents
Ancestor: parent,grandparent,and great grand parent of a node
depth of a node: a length of the path from root to node
height of node : a length of the path from root to node
depth of tree
height of tree

ways to implement tree
1. Linked list
2. Python list(java & Cpp has array)'''

class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[] # list is used to represent the Tree DSA


    def addChild(self,value):
        self.child.append(value)

    def __str__(self,level =0):
        ret = "  "*level +str(self.data)+ "\n"
        for child in self.child:
            ret+=child.__str__(level+1)
        return ret
        

# create nodes
rootNode = Tree("Drinks")
hot = Tree("Hot")
cold = Tree("Cold")
tea = Tree("Tea")
coffee = Tree("Coffee")
nonalcoholic = Tree("Non-Alcoholic")
alcoholic = Tree("Alcoholic")


#add child nodes
rootNode.addChild(hot)
rootNode.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(nonalcoholic)
cold.addChild(alcoholic)

print("Tree Structure:")
print(rootNode)

'''Binary Tree is a special type of tree in which each node can have at most two children, referred to as the left child and the right child.
Key characteristics of a binary tree include:
1. Each node can have at most two children.
2. The tree is hierarchical has one root node.
3. Nodes are connected by edges, forming a parent-child relationship.
Applications of binary trees include:
1. used in searching and sorting algorithms, such as binary search trees (BSTs) and heaps.
2. data compression, expression parsing, and decision-making processes.
3. expression evaluation, Huffman coding, and representing hierarchical data structures.
Types of Binary Trees:
1. Full Binary Tree: A binary tree in which every node has either 0 or 2 children.
2. Complete Binary Tree: A binary tree in which all levels are fully filled except possibly for the last level, which is filled from left to right.
3. Perfect Binary Tree: A binary tree in which all internal nodes have two children and all leaf nodes are at the same level.
4. Balanced Binary Tree: A binary tree in which the height of the left and right subtrees of any node differs by at most one.
5. Degenerate (or pathological) Tree: A binary tree in which each parent node has only one child, resulting in a structure similar to a linked list.'''

#Student Management System
import sys
class CRUD:
    def __init__(self):
        print("Student Management System initialized.")
        self.studentID=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]

    def addStudent(self):
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        rollNo = input("Enter Student Roll Number: ")
        city = input("Enter Student City: ")

        self.studentID.append(id)
        self.studentName.append(name)
        self.studentRollNo.append(rollNo)
        self.studentCity.append(city)

    def showStudents(self):
        print("Student Details are: \n")
        print("Student ID\tStudent Name\tStudent Roll Number\tStudent City")
        for x in range(80):
            print("-", end="")
        print()
        for i in range(len(self.studentID)):
            print(f"{self.studentID[i]}\t\t{self.studentName[i]}\t\t{self.studentRollNo[i]}\t\t{self.studentCity[i]}")

            for x in range(80):print("-", end="")
            print()

    def updateStudent(self):
        id = input("Enter Student Id to update:")
        if id in self.studentID:
            print("1. Student ID:",id)
            print("2. Student Name:",self.studentName[self.studentID.index(id)])
            print("3. Student Roll Number:",self.studentRollNo[self.studentID.index(id)])
            print("4. Student City:",self.studentCity[self.studentID.index(id)])
            print("5. Cancel")
            print("Enter choice to update:")
            choice = input()
            if choice == "1":
                new_id = input("Enter new Student ID: ")
                self.studentID[self.studentID.index(id)] = new_id
            elif choice == "2":
                new_name = input("Enter new Student Name: ")
                self.studentName[self.studentID.index(id)] = new_name
            elif choice == "3":
                new_rollNo = input("Enter new Student Roll Number: ")
                self.studentRollNo[self.studentID.index(id)] = new_rollNo
            elif choice == "4":
                new_city = input("Enter new Student City: ")
                self.studentCity[self.studentID.index(id)] = new_city
            elif choice == "5":
                print("Dont want to update anything.")
                pass
            else:
                print("Invalid choice.")
        else:
            print("Student not found.")

    def deleteStudent(self):
        id = input("Enter Student  ID to delete:")
        if id in self.studentID:
            index = self.studentID.index(id)
            del self.studentCity[index]
            del self.studentRollNo[index]
            del self.studentName[index]
            del self.studentID[index]

    def menu(self):
        while True:
            print("1. Add Student")
            print("2. Show Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.addStudent()
            elif choice == "2":
                self.showStudents()
            elif choice == "3":
                self.updateStudent()
            elif choice == "4":
                self.deleteStudent()
            elif choice == "5":
                sys.exit()
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    crud = CRUD()
    crud.menu()