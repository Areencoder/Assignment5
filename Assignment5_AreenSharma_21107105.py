#Q1
string = input("Enter a string and it will be reversed:")
print("Reversed string:", string[::-1])

#Q2
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)

#Q3
import math
a = int(input("Enter length of first side of the triangle:"))
b = int(input("Enter length of second side of the triangle:"))
c = int(input("Enter length of third side of the triangle:"))
s = (a+b+c)/2   # s = semi-perimeter
if a < b+c and b < a+c and c < a+b:    
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the trianle is",A)
else:
    print("Not a valid triangle!")

#Q4
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#Q5
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#Q6
print("Prime numbers in an input range.")
start = int(input("Enter starting of range(>=2):"))
end = int(input("Enter ending of range:"))
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

#Q7
for i in range(1, 501):
    if i % 7 == 0 and i % 11 == 0:
        print(i)

#Q8
i = 10
l = []
p = []
n = []
odd = []
even = []
Dict = {}
while i > 1:
    num = int(input("Enter integer:"))
    l.append(num)       # make an original list with user inputted integers
    i -= 1
for j in l:
    if j >= 0:          # adds to positive integers list
        p.append(j)
    if j < 0:           # adds to negative integers list
        n.append(j)
    if j % 2 != 0:      # adds to odd integers list
        odd.append(j)
    if j % 2 == 0:      # adds to even integers list
        even.append(j)
    Dict[j] = l.count(j)
print("a) Positive integers:", p)
print("b) Negative integers:", n)
print("c) Odd integers:", odd)
print("d) Even integers:", even)
print('e)')
for k in Dict:
    print(f'integer:{k} ; number of times it occurs: {Dict[k]}')

#Q9
lst = eval(input("Enter a list of words(strings):"))
dct = {}
for i in lst:
    dct[i] = lst.count(i)
for t in dct:
    print(f'word:{t} ; number of times it occurs:{dct[t]}')
