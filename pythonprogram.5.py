def total (a,b):
    result1=a+b
    result2=a-b
    result3=a*b
    result4=a/b
    result5=a^b
    result6=a%b
    print ("function result is", result1)
    print ("function result is", result2)
    print ("function result is", result3)
    print ("function result is", result4)
    print ("function result is", result5)
    print ("function result is", result6)
a=int (input("enter the value of a"))
b=int (input("enter the value of b"))
total (a,b)

x=int (input("enter the value of x"))
y=int (input("enter the value of y"))
total (x,y)



def prasanth (money):
   print("give prasanth the sum of ", money)
money=50
prasanth (money)
prasanth (5*10)
prasanth (5 * 10)

var ='prasanth'
def show():
    global varl
    varl='tall'
    print ("in function var cls",var)
show ()
print ("outside function", varl)
print ("var is ",var)
                                                                                                                                                                                                

def outf() :
    var=10
    def innf():
        var=20
        print ("inner var", var)
    innf() 
    print ("outer var", var)
outf()

def cube (x):
     return(x*x*x)
num=10
result=cube (num)
print("output of the evaluation is", result)

def display(name,age):
    print("name",name)
    print("age",age)
n='prasanth'
y=21
display(name=n,age=y)

def fib(n):
    if n<2:
        return 1
        return(fib(n-1)+fib(n-2))
n=int(input())
for i in range(n):
     print("fibonacci(",i,")",fib(i))

#9
from time import*
t1=perf_counter()
i=sum=0
while i<1000000:
    sum+=1
    i+=1
    sleep(0)
t2=perf_counter()
print("execution time =%f seconds"%(t2-t1))

#10
import datetime
base=datetime.datetime.today()
for x in range (0,10):
    print(base+datetime.timedelta(days=x))


#11
def honai(n,a,b,c):
        if n>0:
            hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
            hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi=(len(a),a,b,c)
print("after puzzle")
print(a,b,c)










