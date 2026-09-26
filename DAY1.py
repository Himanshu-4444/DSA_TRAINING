#wap to remove duplicates
 name = 'prashant'
new_name = ''
for i in name:
    if i not in new_name:
        new_name += i
print(new_name) 

# write a program to accept 3 paper marks M1,M2,M3 and calculate total percentage and check if user is passed in all subject so print pass else print fail and check if percentage is grester than 65 and user is having one project so print he/she eligible for placement drive else print not eligible 
 
M1 = int(input("Enter the marks of M1:"))
M2 = int(input("Enter the marks of M2:"))
M3 = int(input("Enter the marks of M3:"))
total = M1+M2+M3
percentage = total/3.0
print("Total marks:", total)
print("Percentage:", percentage)
if M1>=40 and M2>=40 and M3>=40:
    print("Pass")
    if percentage>65:
        project = input("Do you have a project? (yes/no): ")
        if project.lower() == 'yes':
            print("Eligible for placement drive")
        else:
            print("Not eligible for placement drive")
    else:
        print("Not eligible for placement drive due to low percentage")
else:
    print("Fail") 

 a=[1,2,3,4,5,6,7,8,9,10,11]
a[::2]=10,20,30,40,50,60
print(a) 
 
a=[1,2,3,4,5]
print(a[3:0:-1]) 

 def func(value, values):
    var=1
    values[0]=44
t=3
v=[1,2,3]
func(t,v)
print(t,v[0]) 
 
arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
for i in range(0,4): 
    print(arr[i].pop()) #4,7,11,15  

 def f(i, values=[]):
    values.append(i)
    print(values)
f(1)
f(2)
f(3) 
 
arr =[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1] = arr[i]
for i in range(0,6):
    print(arr[i],end=' ')
 
 
fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1

addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit)) 

 arr = {}
arr[1] = 1
arr['1']=2
arr[1] +=1
print(arr)
sum=0
for k in arr:
    sum += arr[k]
print(sum) 
 
my_dict = {}
my_dict[1] =1
my_dict['1'] = 2
my_dict[1.0]=4
print(my_dict)
sum=0
for k in my_dict:
    sum += my_dict[k]   
print(sum) 

 my_dict = {}
my_dict[(1,2,4)]=8
my_dict[(4,2,1)]=10
my_dict[(1,2)]=12
sum=0
for k in my_dict:
    sum += my_dict[k]
print(sum)
print(my_dict) 

 box={}
jars={}
crates={}
box['biscuit']=1
box['cake']=3
jars['jam']=2
crates['box']=box
crates['jars']=jars
print(len(crates[box])) 

 dict ={'C':97,'A':96,'B':98}
for _ in sorted(dict):
    print(dict[_]) 

 rec ={'name':'pyhton','age':20}
r=rec.copy()
print(id(r)==id(rec))
print(id(r))
print(id(rec)) 

 arr =[0,1,0,3,12]
for i in arr:
    if i==0:
        arr.remove(i)
        arr.append(0)
print(arr) 

 arr = [7,3,9,2,8]
second_largest = arr[0]
largest = arr[0]
for i in arr:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest and i!=largest:
        second_largest = i
print("Second largest:", second_largest) 

 arr=[1,2,3,4] #from both side multiply all elements except itself right to left and left to right
for i in arr:
    product=1
    for j in arr:
        if i!=j:
            product *= j
    print(product,end=' ') 

 A=[1,2,3]
B=[2,3,4]
C=[3,4,5]
for i in A:
    if i in B and i in C:
        print(i) 

 arr =[1,1,0,1,1,1,0,1,1,1,1]
count=0
for i in arr:
    if i==1:
        count += 1
    else:
        count=0
print(count) 

 #wap to accept any single chr and check the entered chr is in uppercase ,lowercase,digit or special chr and print msg accordingly
chr = input("Enter a single character: ")
if chr.isupper():
    print("The character is in uppercase.")
elif chr.islower():
    print("The character is in lowercase.")
elif chr.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.") 

inp='helpforcode'
count_vowels=0
count_consonants=0
for i in inp:
    if i in 'aeiouAEIOU':
        count_vowels += 1
    elif i.isalpha():
        count_consonants += 1
print("Number of vowels:", count_vowels)
print("Number of consonants:", count_consonants)
