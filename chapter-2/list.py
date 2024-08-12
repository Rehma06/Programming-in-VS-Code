#creating a list
fruit=['apple','banana','cherry']
#using list
print(fruit)
print(fruit[2])
#slicing
print(fruit[0:2])
#putting a variable equals to another
fruit1=fruit
print(fruit1)
#changing a value in the list
fruit[2]='date'
print(fruit)
#putting a variable equal to another using copy
fruit2=fruit.copy()
print(fruit2)
#changing a value again
fruit[1]='strawberry'
print(fruit2)
print(fruit)