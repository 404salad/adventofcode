with open("input.txt","r") as file:
    ans = 0
    for line in file.readlines():
        stuff = line[:-1].split()
        stuff1=list(map(int,stuff[2:12:]))
        stuff2=list(map(int,stuff[13:]))
        mul = 1/2
        for el in stuff2:
            if el in stuff1:
                mul*=2
        if(mul!=0.5):
            ans+=mul
        print(mul)
    print(int(ans))

