
cubes=[i**3 for i in range(11)]
print(cubes)

term = int(input("enter the turm"))
if term%2 ==0:
    term = term//2
    print(3**(term-1))
else:
    term=term //2+1
    print(2**(term-1))
