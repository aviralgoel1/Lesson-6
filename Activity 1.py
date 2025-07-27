while True:
    word=str(input("Enter a word: "))
    letter=str(input("What letter do you want to find: "))

    i=0
    count=0

    while(i<len(word)):
        if(word[i] == letter):
            count = count + 1
        i=i+1
    print(count)