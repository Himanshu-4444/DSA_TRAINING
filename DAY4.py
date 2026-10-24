'''wap to accept roll number, name, mobile number, p1,p2,p3,emmail
calculate total and percentage 
condition chekc if user is passed in all the subjects so store 'pass' in result colum else store 'fail' and passing marks will be 40'''
import csv
f = open("students.csv", "a",newline="")
a=csv.writer(f)
a.writerow(["studentID","rollno","name",'mobileno','p1','p2','p3','total','percentage','email']) # devlop logic to write this line once only
studentID = input("Enter student ID: ")
rollno = input("Enter roll number: ")
name = input("Enter student name: ")
mobileno = input("Enter mobile number: ")
p1 = input("Enter marks for subject 1: ")
p2 = input("Enter marks for subject 2: ")
p3 = input("Enter marks for subject 3: ")
email = input("Enter email: ")
total = int(p1) + int(p2) + int(p3)
percentage = (total / 300) * 100
if int(p1) >= 40 and int(p2) >= 40 and int(p3) >= 40:
    result = "pass"
else:
    result = "fail"
a.writerow([studentID, rollno, name, mobileno, p1, p2, p3, total, percentage, email])
print("Data written successfully to students.csv")

'''The manager of a supermarket wants to organize an event in which he will distribute gift hampers to the winners of the event. The manager has planned it in such a way that each customer has to pick the product in a pair, and each pair has different types of products.
Any two customers can't pick the same type of product pair, but the price may be the same. There are N types of products, and each product has a price. He will offer the gift hampers to those customers for whom the difference in the prices of the products picked is equal to the given integer value K.
Write an algorithm to help the manager find the total number of lucky customers who will get the gift hampers.
INPUT:
ProductTypes: An integer representing the types of products (N).
numK: An integer representing the given value K.
prices: A list of integers representing the prices of the products.
OUTPUT:
Print the total number of lucky customers who will get the gift hampers.'''

n = int(input("Enter the number of product types: "))
k = int(input("Enter the value of K: "))
prices = list(map(int, input("Enter the prices of the products: ").split()))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if abs(prices[i] - prices[j]) == k:
            count += 1

print("The total number of lucky customers who will get the gift hampers is:", count)

class Node:
    def __init__(self, value):
        #every node will contain data and a pointer to the next node
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linkedListObj=LinkedList()
# crate seprate nodes/memory
linkedListObj.head=Node(10)
secondNode=Node(20)
thirdNode=Node(30)
fourthNode=Node(40)
fithNode=Node(50)

#connecting nodes
linkedListObj.head.next=secondNode
secondNode.next=thirdNode
thirdNode.next=fourthNode
fourthNode.next=fithNode

#display linked list
while linkedListObj.head != None:
    print("|",linkedListObj.head.data,"|",end="->")
    linkedListObj.head=linkedListObj.head.next
    

class Node:
   def __init__(self, value):
        #every node will contain data and a pointer to the next node
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # head is going to represent the starting node 
        self.tail = None  # tail is going to represent the end node 

# add node in the end
    def addNodeEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def display(self):
        current = self.head
        while current is not None:
            print("|", current.data, "|", end="->")
            current = current.next
        print("None")  # Indicate the end of the linked list

linkedListObj = LinkedList()
linkedListObj.addNodeEnd(10)
linkedListObj.addNodeEnd(20)
linkedListObj.addNodeEnd(30)
linkedListObj.display()