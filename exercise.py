# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
a = 123
b = type(a)
print(a,b,sep=" is type of ")

c = 589
d = type(c)
print(c,d,sep=" complete type of")

e = 43.23
hb = type(e)
print(a,b,sep=" is type of ")


a = (4-1j)
b = type(a)
print(a,b,sep=" is type of ")


a = "Welcome to Barcelona"
b = type(a)
print(a,b,sep=" is type of ")

a = True
b = type(a)
print(a,b,sep=" is type of ") 

H = "hELLO wORLD"
print(H)


a = 123
b = isinstance(a,int)
print(a,b)

c = 458
d = isinstance(c,int)
print(c,d)
e = 456
f = isinstance(e, int)
print(c,d)

c = 456
d = isinstance(a, int)
print(c, d)

a = 42.23
b = isinstance(a, float)
print(a,b)



a = True
b = isinstance(a, bool)
print(a,b)

a = (4+2j)
b = isinstance(a, complex)
print(a,b)

a = "hello"
b = isinstance(a, str)
print(a,b)


a = 123
b = isinstance(a, int)
print(a,b)


a = 42.23
b = isinstance(a, float)
print(a,b)

a = True
b = isinstance(a, bool)
print(a,b)

a = (4+2j)
b = isinstance(a, complex)
print(a,b)

a = "hello"
b = isinstance(a, str)
print(a,b)


g =  7/9
print(round(g,7)) 


"""4"""


a = 123
b = int
c = isinstance(a, b)
print("is",a, "in an instance of:",b,"?",c)



a = 123
b = int
c = isinstance(a, b)
print("is",a, "in an instance of bool?:",c)

a = 42.23
b = bool
c = isinstance(a, b)
print("is",a, "in an instance of float?",c)

a = (4-1j)
b = complex
c = isinstance(a, b)
print("is",a, "in an instance of complex?",c)

a = True
b = bool
c = isinstance(a, b)
print("is",a, "in an instance of bool",c)


a = "how are you?"
b = float
c = isinstance(a, b)
print("is",a, "in an instance of float",c)

c = "We are going to Munich"
d = float
e = isinstance(c,d)
print ("is",a,"in the instance of float", e )

###
x = 5
y = 3

print(x - y)

x = 45
y = 30
print(x -y)



x = 5
y = 3

print(x - y)

x = 45
y = 30
print(x -y)



x = 43
y = 56
print(x -y)

x = 4
y = 4
print(x * y)



x = 4
y = 5
print(x /y )


a = 12
b = 5
print(a % b) 


import math
x = 89
y = 5
print(math.floor(89/5))

x = 89
y = 8
print(math.ceil(89/5))

12.2 // 3 

x = 12.2
y = 3
print(math.floor(12.2/3))


a = 3
b = 4
x = 12.2
y = 3
print(math.floor(12.2/3))


a = 3
b = 4
print(math.pow(3,4))



#
n = 300 
m = 400

if n > m: 
    print("n is less than m")
else: 
    print("m is more than n")
         

a = 30
b = 39
c = 45
if a < b:
    if  b > c:
         print("a is less than b")
    else:
        print("b is less than c")
else:
    print("a is greater than b")
    
x = 12.2
y = 3
print(math.floor(12.2/3))


a = 3
b = 4
print(math.pow(3,4))



#
n = 300 
m = 400

if n > m: 
    print("n is less than m")
else: 
    print("m is more than n")
         

a = 30
b = 39
c = 45
if a < b:
    if  b > c:
         print("a is less than b")
    else:
        print("b is less than c")
else:
    print("a is greater than b")
    
   # 
    x = 50
    y = 100
    print((x, y))

   # 
    x = 50
    y = 100
    print((x, y))

print(math.pow(3,4))



#
n = 300 
m = 400

if n > m: 
    print("n is less than m")
else: 
    print("m is more than n")
         

a = 30
b = 39
c = 45
if a < b:
    if  b > c:
         print("a is less than b")
    else:
        print("b is less than c")
else:
    print("a is greater than b")
    
   # 
    x = 50
    y = 100
    print((x, y))

#
for i in range(3):
    print(i)
    for i in range(3,2,8):
        print(*range(3,2,8))

    #
    x = range(4,2,10)
    for n in x:
        print(n)

 
x = range(2, 8, 2)
for n in x:
  print(n)

num = int(input("Enter a Number 63:"))
if num % 2 == 0:
  print(num , "is even")
else:
  print(num , "is odd")

  num = int(input("Enter a number 63: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

num  = int(input("please Enter the Max number 56:"))
for number in range(1, num+1):
    if(number % 2 ==0):
        print("{0}is Even".format(number))
       ## 
for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        
    elif fizzbuzz % 3 == 0:
        print("fizz")
        
    elif fizzbuzz % 5 == 0:
        print("buzz")
        
    print(fizzbuzz)


#

for index in range(1000,2000):
    index +=1
    if index % 5 == 0 and index % 7 == 0:
        print(index)

for i in range(2, 6):

    print(i)
    #

for x in range(10):
    pass

numbers  =  range(6)
numbers_list = list(numbers)
print(numbers_list)

numbers = range(10)
numbers = numbers(numbers)
print(numbers)