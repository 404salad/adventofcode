with open("input.txt","r") as file:
    lawn = 204 
    ans = []
    for i in range(lawn):
        ans.append(1) 
    for i,line in enumerate(file.readlines()):
        stuff = line[:-1].split()
        stuff1=list(map(int,stuff[2:12:]))
        stuff2=list(map(int,stuff[13:]))
        count=0
        for el in stuff2:
            if el in stuff1:
               count+=1 
        print(i,ans[i],count)
        for z in range(count):
            if(i+z<lawn):
                ans[i+z]+=ans[i-1]
                
    print(list(map(int,ans)))
    print(sum(list(map(int,ans))))

