'''write a program to calculate and return the sum of distance between the adjacent numbers between array of position integers. 
input = 5  [10,11,7,12,14]
output = 12'''

def sum_of_distances(arr):
    total_distance = 0 #variable to store the total distance
    for i in range(len(arr) - 1):
        total_distance += abs(arr[i] - arr[i + 1])  
    return total_distance   
print(sum_of_distances([10, 11, 7, 12, 14])) #output = 12

# or 
n = int(input("Enter the number of elements in the array: "))
my_list = list(map(int,input().split()))
sum = 0 
for i in range(n-1):
    sum += abs(my_list[i] - my_list[i+1])
print("Sum=", sum) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question: Write a program to find the first even number in a list of roll numbers. If an even number is found, print it; otherwise, print "even not found".
roll_num = [3,5,7,1,11,4,5,2]
for x in roll_num:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print(x, "even not found")
        break 
    else:
        print("even not found")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 2: Write a program to print the following pattern

for i in range(1,4):#outer loop - represents the rows
    for j in range(1,4):#inner loop - represents the columns
        print(i, end=" ")#print the value of i and stay on the same line
    print()#print a new line after each row
    

'''(i,j)= (2,1)
       1 2 3
 1     1 1 1
 2     2 2 2
 3     3 3 3'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#Question 3: Write a program to print the following pattern
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + i), end=" ")  # Print the character corresponding to the row number ASCII value (A=65, B=66, C=67, ...)
    print()  # Move to the next line after each row
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#Question 4: Write a program to print the following pattern
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()  # Move to the next line after each row   

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question 5: Write a program to print the following pattern descending order   
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(n+1-i, end=" ")
    print()
'''For n = 3, expected output:
3 3 3
2 2 2
1 1 1'''

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question : add all * in prefix
'''input = prashant*is*a*good*programmer
output = ****prashantisagoodprogrammer'''

name = "prashant*is*a*good*programmer"
new = ''
val = ''
for i in name:
    if i != '*':
        new += i
    else:
        val += i
print(new)
print(str(val+new)) 

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#question : find the maximum number from each row of a 2D array
arr = [[100,198,333,323],[122,232,221,111],[223,565,245,764]]
#exxpected output = 333,232,764 (maximum number from each row)
for row in arr:
    print(max(row), end=", ")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Question: Write a program to calculate the total bill amount for a customer based on the number of items purchased.
#The program should prompt the user to enter the quantity of each item and then calculate the total bill amount based on the following prices:
pizza = 100
burger = 50
coldrink = 20
val1 = int(input("Enter the number of pizza: "))
val2 = int(input("Enter the number of burger: "))
val3 = int(input("Enter the number of coldrink: "))
pizza_total = pizza * val1
burger_total = burger * val2
coldrink_total = coldrink * val3
print("-----------------------------------------------")
print("Bill Details")
print("Pizza: ", pizza_total)  
print("Burger: ", burger_total)
print("Coldrink: ", coldrink_total)
print("Total: ", pizza_total + burger_total + coldrink_total)
print("-----------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question : WAP check two arrays are compatible or not
A = []
B = []
n1 = int(input("Enter the size of first array: "))
for i in range(n1):
    A.append(input())

n2 = int(input("Enter the size of second array: "))
for i in range(n2):
    B.append(input())

# Check if arrays are compatible
if len(A) == len(B):
    print("Arrays are compatible")
else:
    print("Arrays are not compatible")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Question :Description

'''You are playing an online game. In the game, a list of N numbers is given. The player has to arrange the numbers so that all the odd numbers ers of the list come after the even numbers. Write an algorithm to arrange the given list such that all the odd numbers of the list come after the even numbers.

Input

The first line of the input consists of an integer num, representing the size of the list (N).

The second line of the input consists of N space-separated integers representing the values of the list.

Output

Print N space-separated integers such that all the odd numbers of the list come after the even numbers.'''


n = int(input("Enter the size of the list: "))
list = list(map(int, input("Enter the numbers: ").split()))
odd = ''
even = ''
for i in range(1, n + 1):
    if i % 2 == 0:
        even += str(i) + ' '
    else:
        odd += str(i) + ' '
        
print(even+odd)
#--------------------------------------------------------------------------------------------------------------------------------------
#Question: CRUD Operation
import sys 
class CRUD:
    def __init__(self):
        print("School Management System")
        self.studentsid = []
        self.studentsname = []
        self.studentrollno = []
        self.studentcity = []
        
    def add_student(self):
        self.studentsid.append(input("Enter student ID: "))
        self.studentsname.append(input("Enter student name: "))
        self.studentrollno.append(input("Enter student roll number: "))
        self.studentcity.append(input("Enter student city: "))
        
    def show_students(self):
        if not self.studentsid:
            print("No student records found.")
            return

        id_width = max(len("Student ID"), max(len(student_id) for student_id in self.studentsid))
        name_width = max(len("Name"), max(len(name) for name in self.studentsname))
        roll_width = max(len("Roll Number"), max(len(roll_no) for roll_no in self.studentrollno))
        city_width = max(len("City"), max(len(city) for city in self.studentcity))

        total_width = id_width + name_width + roll_width + city_width + 12

        print("Student Details")
        print(f"{'Student ID':<{id_width}} {'Name':<{name_width}} {'Roll Number':<{roll_width}} {'City':<{city_width}}")
        print("-" * total_width)

        for i in range(len(self.studentsid)):
            print(f"{self.studentsid[i]:<{id_width}} {self.studentsname[i]:<{name_width}} {self.studentrollno[i]:<{roll_width}} {self.studentcity[i]:<{city_width}}")

        print("-" * total_width)
    
    def update_student(self):
        id = input("Enter student ID to update: ")
        if id in self.studentsid:
            index = self.studentsid.index(id)
            self.studentsname[index] = input("Enter new student name: ")
            self.studentrollno[index] = input("Enter new student roll number: ")
            self.studentcity[index] = input("Enter new student city: ")
        else:
            print("Student ID not found.")
    
    def delete_student(self):
        id = input("Enter student ID to delete: ")
        if id in self.studentsid:
            index = self.studentsid.index(id)
            del self.studentsid[index]
            del self.studentsname[index]
            del self.studentrollno[index]
            del self.studentcity[index]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

    def start(self):
        while True:
            print("1. Add Student")
            print("2. Show Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.show_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    obj = CRUD()
    obj.start()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#QUEUE DATA STRUCTURE 
class Queue:
    def __init__(self, size):
        self.queueSize = size
        self.myqueue = [] #implementing queue using list
    
    def isFull(self):
        if len(self.myqueue) == self.queueSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.myqueue == []:
            return True
        else:
            return False
    def enQueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            self.myqueue.append(data)
            print("Enqueued:", data)
    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            data = self.myqueue.pop(0)
            print("Dequeued:", data)
    def peek(self): #returns the first element of the queue
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("First element:", self.myqueue[0])
    def deleteQueue(self):
        self.myqueue = []
        print("Queue deleted")
    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.myqueue)

size = int(input("Enter the size of the queue: "))
obj = Queue(size) #creating object of queue class , constructor will be called automatically and size will be passed to the constructor
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek Front Element")
    print("4. Display Queue")
    print("5. Delete Queue")
    print("6. Check if Queue is Full")
    print("7. Check if Queue is Empty")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = input("Enter the element to enqueue: ")
        obj.enQueue(data)
    elif choice == '2':
        obj.deQueue()
    elif choice == '3':
        obj.peek()
    elif choice == '4':
        obj.displayQueue()
    elif choice == '5':
        obj.deleteQueue()
    elif choice == '6':
        if obj.isFull():
            print("Queue is full")
        else:
            print("Queue is not full")
    elif choice == '7':
        if obj.isEmpty():
            print("Queue is empty")
        else:
            print("Queue is not empty")
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please try again.")
