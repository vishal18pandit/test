#Assignment-2 	Day-2		02-June-2020 	


#1. Write a Python program to swap two elements in a list.

def swapPositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
List =[23,65,7,4]
print("list before swapping",List)
pos1,pos2=2,3
print("after swapping = ",swapPositions(List,pos1-1,pos2-1))
​


#2. Write a Python program for Reversing a List.

list  = ["apple","mango","grapes"]
list.reverse()
print(list)


#3. Write a Python program to Multiply all numbers in the list.

res=1
list = [2,3,4]
​
for x in list:
    res=res*x
print(res)



#4. Write a Python program to interchange first and last elements in a list

list = [2,3,4,5,6]
n=len(list)
print("list before interchange",list)
list[0],list[n-1]=list[n-1],list[0]
print("list after interchange",list)
​



#5. Write a Python program to find largest number in a list

lst = []
n=int(input("enter number of elements"))
for i in range(0,n):
    ele=int(input())
    
    lst.append(ele)
print(lst)
​
print("Largest number from list =",max(lst))





#6. Write a Python program to find the sum of all items in a dictionary.

def returnSum(dict): 
      
     sum = 0
     for i in dict.values(): 
           sum = sum + i 
       
     return sum
 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict))



# 7. Write a Python program for Merging two Dictionaries.

def Merge(dict1, dict2): 
    return(dict2.update(dict1)) 
 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 

print(Merge(dict1, dict2)) 

print(dict2) 






#8. Write a Python script to sort (ascending and descending) a dictionary by
value.

import operator  
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}  
print('Original dictionary : ',d)  
sorted_d = sorted(d.items(), key=operator.itemgetter(0))  
print('Dictionary in ascending order by value : ',sorted_d)  
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)  
print('Dictionary in descending order by value : ',sorted_d)  







#9. Write a Python script to check whether a given key already exists in a
dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)









#10. Write a Python program to remove a key from a dictionary.



myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)



#11. Write a Python program to create a tuple with different data types.

tuplex = ("tuple", False, 3.2, 1)
print(tuplex)








#12. Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)







#13. Write a Python program to find the repeated items of a tuple.

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(tuplex)

count = tuplex.count(4)
print(count)





#14. Write a Python program to convert a list of characters into a string.

s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)


#15. Write a Python program to append a list to the second list.

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)
