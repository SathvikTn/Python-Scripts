#for pycharm, use "if __name__ == '__main__': " before the code to run the code.

#7 Tricks of python
#list comprehension
#before
def square():
    x = list(map(int, input().split()))
    y = []
    for i in x:
        if i > 2:
            y.append(i**2)
    print(y)
#square()

#after
def squares():
    x = list(map(int, input().split()))
    y = [i**2 for i in x if i > 2]
    print(y)
#squares()

#lambda function

x = [1,2,3,4,5]

sq = lambda x:x**2
print(sq(10))       #x gets 10 and prints x^2 = 100
print([sq(i) for i in x])    #passing elements of list to lambda function
print(list(map(lambda i:i*10,x)))  #mapping every ele of x to lambda function

def s(n):
    return lambda x:x*n    #n is given, for any x, return x*n
double = s(2)             #function where n = 2
print(double(10))         #function where n = 2 and x = 10..so 20 is ans

#map
def a(i):
    return i**2
x = [4,7,9]
print(list(map(a,x))) #maps all ele of x to a

#filter
def z(i):
    return i>2   #to print only ones that are greater than 2
x = [1,2,3,4,5]
print(list(filter(z,x)))

#join
x = ['1','2']
print(" ".join(x)) #join ele of x with spaces in between

#enumerate - add counters to data
x = [5,6,7,8,9]
print(list(enumerate(x,start=0)))  #start the counter from 0

#format - to edit the string
a = "{0} {1} of python"
print(a.format(7,'tricks'))
print(a.format('top 7','functions'))