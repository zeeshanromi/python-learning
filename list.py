# lists
# index checking....
fruits = ["apple","orange","grapes"]
marks = [45, 34, 89,76,76,59 ]
print(marks[3])
print(marks[-2])

# index slicing..
print(marks[1:3])
print(marks[:4])

# append method...
marks.append(80)
print(marks)

# sort method...
fruits.sort() # in ascending order
print(fruits)
marks.sort() 
print(marks)
marks.sort(reverse=True) # descending order
print(marks)
fruits.sort(reverse=True)
print(fruits)

# insert method 
fruits.insert(1, 'banana')
print(fruits)
marks.insert(4,98)
print(marks)

# remove method 
marks.remove(76) # to remove number vise
print(marks)
fruits.remove('orange')
print(fruits)
marks.pop(5)
print(marks)
fruits.pop(2)
print(fruits)