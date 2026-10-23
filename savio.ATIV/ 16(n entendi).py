a=int(input("digiti um numero"))
b=int(input("digiti outro numero"))
c=int(input("digiti outro numero"))
if a>b and a>c:
    maior=a
elif b>a and b>c:
    maior=b
else:
    maior=c
x=a
y=b
if x**2+y**2 == maior **2:
    print("Os três números formam um triângulo retângulo")
else:
    print("Os três números não formam um triângulo retângulo")