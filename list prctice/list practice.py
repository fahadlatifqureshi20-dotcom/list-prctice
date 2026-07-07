fruits = ["Apple", "Banana", "Mango"]
print(fruits)

#empty list 
my_list = []
print(my_list)

#fruits list 
fruits = ["Apple", "Banana", "Mango", "Orange", "pineapple"]
print(fruits)

#length of list 
print(len(fruits))

#printing first element of list 
print(fruits[0])

#last element 

print(fruits[-1])

#second element 

print(fruits[1])

#new element add

fruits.append("Grapes")

print(fruits)

#inserting 
fruits = ["Apple", "Banana", "Mango"]

fruits.insert(0, "Grapes")

print(fruits)

#checking if apple is in list or not 

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

if "Apple" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")


#removing element from list

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

fruits.remove("Mango")

print(fruits)

#removing last element from list 

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

fruits.pop()

print(fruits)

#second day work 
#saving list in ascending order
fruits.sort()
print(fruits)

#saving list in descending order
fruits.sort(reverse=True)
print(fruits)

#reversing the list
fruits.reverse()
print(fruits)

#copying the list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]   
fruits_copy = fruits.copy()
print(fruits_copy)

#combining two lists
fruits = ["Apple", "Banana", "Mango"]   
vegetables = ["Tomato", "Potato", "Cabbage"]   
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

#combining a list to other list from the end
fruits = ["Apple", "Banana", "Mango"]   
fruits.extend(vegetables)
print(fruits)

#printing the list using for loop
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for fruit in fruits:
    print(fruit)

#printing even numbers from list
numbers = [1, 2, 3, 4, 5, 6 ]
for number in numbers:
    if number % 2 == 0:
        print(number)
        
#remoing a specific element from list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for i in fruits:
    if i == "Mango":
        fruits.remove(i)
print(fruits)

list1 = [1, 2, 3, 4, 5]
for i in list1:
    if i == 4:
       list1.remove(i)

print(list1)

#loops and logic 
fahad_list=[]
for i in range (21):
    fahad_list.append(i)

print(fahad_list)

#sum of all numbers in list
print(sum(fahad_list))

#finding the largest number in list
if fahad_list:
    largest_number = fahad_list[0]
    for i in fahad_list:
        if i > largest_number:
            largest_number = i
    print(largest_number)
else:
    print("List is empty")  

#finding the smallest number in list
if fahad_list:
    smallest_number = fahad_list[0]
    for i in fahad_list:
        if i <smallest_number:
            smallest_num=i
    print(smallest_number)


#finding average of numbers in list
if fahad_list:
    average = sum(fahad_list) / len(fahad_list)
    print(average)  

#finding even and odd numbers in list
even_numbers = []
odd_numbers = []
for i in fahad_list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

evn=[]
odd=[]
for i in fahad_list:
    if i%2==0:
        evn.append(i)
    else:
        odd.append(i)
print('Number of even numbers:', len(evn))
print('Number of odd numbers:', len(odd))

#creating a list of squares of numbers in fahad_list
squares = []
for i in fahad_list:
    squares.append(i ** 2)
print('Squares of numbers:=', squares)  

#checking duplicate elements in list
my_list1 = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
duplicates = []
for i in my_list1:
    if my_list1.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print('Duplicate elements:=', duplicates)

#slicing question...........................

#printing first three elements of list
fahad_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first_three = fahad_list[:3]
print('first three elements:=', first_three)

#using for loop to print first three elements of list
fahad_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
first3 =[]
for i in range(3):
    first3.append(fahad_list[i])
print('first three elements using loop :=', first3)

#last three elements of list
fahad_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
last_three = fahad_list[-3:]
print('last three elements:=', last_three)

#printing middle four elements of list
fahad_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
middle_four = fahad_list[8:12]
print('middle four elements:= ',middle_four)

#printing every numbr in the list with the gap of 2 

fahad_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(fahad_list[0:19:2])