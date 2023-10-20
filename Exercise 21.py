a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
ab=a+b
ac=a+c
bc=b+c
if a<bc and b<ac and c<ab:
    print ("This triangle exists")

if a>bc or b>ac or c>ab:
    print("This triangle does not exist")