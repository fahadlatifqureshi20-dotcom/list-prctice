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