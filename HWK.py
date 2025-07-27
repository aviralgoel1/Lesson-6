while True:
    n=int(input("enter a number: "))
    a=abs(n)
    bin=""

    while a!=0:
        x=a%2
        a=a//2
        bin=str(x)+str(bin)

    if n>0:
        print(bin)
    elif n<0:
        print("-"+bin)
