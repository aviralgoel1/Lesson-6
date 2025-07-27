while True:
    n=int(input("enter a number: "))
    x=1

    if n>0:
        for num in range (1,n+1):
            x=num*x
        print (x)
    else:
        print("Type a number more than 1")