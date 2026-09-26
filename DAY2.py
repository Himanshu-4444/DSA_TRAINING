# Day 2 Training
# example of stack is brower history, undo operation in text editor, function call stack
# how Many ways to implement stack in python
# 1. Using a list(easy to implement speed problem when it grows)
# 2. Using a linked list(fast performance but complex to implement)
class Student:
    rollno = 101  #data member of class
    def __init__(self):
        print("Constructor is called")
    def msg(self):
        print("Hello")
obj = Student()
print(obj)
obj.msg()
obj1 = Student()
print(obj.rollno)

class Hod:
    def __init__(self):
        self.name = "Prashant Jha"
        self.age = 53
        self.empid = 1001
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Empid:",self.empid)

hod = Hod()
hod.info()

class Hod:
    def __init__(self,name,age,rollno): #parameterized constructor is used to initialize the data members of the class with the values passed as arguments when an object is created
        self.name = name
        self.age = age
        self.empid = rollno
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Empid:",self.empid)

hod = Hod("Arjun", 45, 101)
hod.show()

#create a class name of students and accept personal info like name, mobileno, emailid and creare a method to dispaly the personal info 

class Student:
    def __init__(self, name, mobile_no, email_id):
        self.name = name
        self.mobileno = mobile_no
        self.emailid = email_id
    def display_info(self):
        print("Name:", self.name)
        print("Mobile No:", self.mobileno)
        print("Email ID:", self.emailid)

student = Student(input("Enter name: "), int(input("Enter mobile number: ")), input("Enter email ID: "))
student.display_info()

class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.mobileno = int(input("Enter mobile number: "))
        self.emailid = input("Enter email ID: ")
        self.rollno = int(input("Enter roll number: "))
        self.branch = input("Enter branch: ")
obj = Student()
print(obj.__dict__) #__dict__ is a built-in attribute that returns a dictionary containing the object's attributes and their values. It allows you to access and manipulate the object's data in a structured way.

# Implementing a Stack using a list & max element in O(1) time complexity
import sys
class Stack:
    def __init__(self, size): #constructor is always called first when an object is created it create memory for the object and initialize the address of the object
        self.stackSize = size
        self.myStack = []

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.myStack) == 0: # or self.myStack == []:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Stack is full. Cannot push", data)
        else:
            self.myStack.append(data)
            print(data, "pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop.")
        else:
            popped_value = self.myStack.pop()
            print(popped_value, "popped from stack")

    def peek(self):
        if self.isEmpty():
            print("stack is empty. Cannot peek.")
        else:
            print("Top element is:", self.myStack[-1])

    def deleteStack(self):
        self.myStack = []
        print("Stack deleted.")

    def displayStack(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to display.")
        else:
            print("Stack elements are:", self.myStack)
    def getMaxElement(self):
        if self.isEmpty():
            print("Stack is empty. No max element.")
            return None
        else:
            max_element = max(self.myStack)
            return max_element

    def __str__(self):
        return "Stack size: {}, Stack elements: {}".format(self.stackSize, self.myStack)
    

size = int(input("Enter the size of the stack: ")) #execution starts from here
obj = Stack(size)

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. isEmpty")
    print("5. isFull")
    print("6. Get max element")
    print("7. Delete Stack")
    print("8. Display Stack")
    print("9. Exit")

    choice = int(input("Enter your choice:"))
    print("DEBUG: Choice received =", choice)
    if choice == 1:
        value = int(input("Enter the value to push in the stack: "))
        obj.push(value)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        if obj.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    elif choice == 5:
        if obj.isFull():
            print("Stack is full.")
        else:
            print("Stack is not full.")
    elif choice == 6:
        print("Max element in the stack is:", obj.getMaxElement())
    elif choice == 7:
        obj.deleteStack()
    elif choice == 8:
        obj.displayStack()
    else:
        sys.exit()