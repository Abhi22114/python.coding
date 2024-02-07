
# Write Python 3 code in this online editor and run it.
#function:-function is a block of code that only runs when it called ,,manage the 
#input and output inthe computer systems:-
#def printText():
    #print("1")
    #print("heloo world ")
    #print(3)
    
#print('hello')
#printText()
#print("abhijeet")
#print("India is going to lifted this world cup")
#printText()

#def printName(name,age):
    #print('My name is'+ name +" and My age is" + age)
#print('abhijet','10')
def printSum(num1, num2):
     print(num1 + num2)
printSum(10,20)
printSum(20,40)

#arbitaroy arguments
#when we are not sure about the number arugments that can be passed inside 
# a function using add* to function

# aribtrary arguments

# when we are not sure about the number arguments that can be passed inside a function, add * to the parameter


# def myName(*name):
#     print('My name is ' + name[2])
#     print(name)


# myName('John', 'Peter', 'Raj')

# key words arguments
# we can send the aruguments in the form gor key = value

# def myName(name3, name1, name2):
#     print('My name is ' + name3)


# myName(name1='John',name2= 'Peter',name3= 'Raj')

# myName('John', 'Peter', 'Raj')
# key words arguments
# we can send the aruguments in the form gor key = value

# def myName(name3, name1, name2):
#     print('My name is ' + name3)


# myName(name1='John',name2= 'Peter',name3= 'Raj')

# myName('John', 'Peter', 'Raj')

# arbitrary keyword arguments
# **kwargs


# def myName(**name):
#     print(name)
#     print( 'my name is ' + name["name2"])


# myName(name1='John',name2= 'Peter',name3= 'Raj')







#defult parameters

def myFunc(age ='40'):
    print('My age is '+age )

myFunc('10')
myFunc('34')
myFunc()

#def printFruits(fruits):
    #print(fruits)
    #for fruits in fruits:
        #print(fruits)
#fruits=['apples ','bananas','oranges']
#printFruits(fruits)

#def printAge():
    #print(10)
    #print(20)
    #return 20
def myFunc(x):
    return 2*x
    
print(myFunc(5))
print(myFunc(6))


