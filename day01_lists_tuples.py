# Create a list of 5 numbers and print the entire list

numbers= [1,2,3,4,5]
print("numbers=",numbers)

# Create a list of 5 fruits. Print the first fruit and the last fruit

fruit= ["Mango","Apple","Cherry","Banana","Berry"]
print(fruit[0])
print(fruit[-1])

# Create a list of numbers [10, 20, 30, 40, 50]. Print the first three elements
 
number= [10, 20, 30, 40, 50]
print(number[0:3])

# Create a list of 3 colors. Add one more color using append()
colors= ["pink","YEllow","Green"]
colors.append("Purple")
print("colors=",colors)

# Given numbers = [5, 10, 15, 20], remove 10 from the list
numbers= [5, 10, 15, 20]
numbers.remove(10)
print("numbers= ",numbers)

# Create a tuple containing 5, 10, 15, 20. Print the second element
myTuple= (5,10,15,20)
print(myTuple[1])

# Create a tuple of 4 animals. Print the first and last animals.
Animals= ("Cat","Dog","pig","Rat")
print(Animals[0])
print(Animals[-1])

# Create a tuple of 5 numbers. Print the first three elements using slicing.
numbers= (1,2,3,4,5)
print(numbers[0:3])

# Find the length of this list: [2, 4, 6, 8, 10, 12]
num= [2, 4, 6, 8, 10, 12]
print(len(num))

# . Find how many times 2 occurs in the tuple (1, 2, 2, 3, 2, 4)
num= (1, 2, 2, 3, 2, 4)
print(num.count(2)) 