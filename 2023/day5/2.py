with open("input.txt") as file:
    #parse input
    sab = []
    seeds = []
    splitfile = file.read().split("\n\n")
    for i,line in enumerate(splitfile):
        if(i==0):
            seeds=line[6:].split()
            continue
    actualseeds=[] 
    print(seeds)
    """
    for zed in range(int(seeds[0]),int(seeds[0])+int(seeds[1])):
        actualseeds.append(zed) 
    for zed in range(int(seeds[2]),int(seeds[3])+int(seeds[3])):
        actualseeds.append(zed) 
    """
    print(actualseeds)
    seeds = actualseeds
    for seed in seeds:
        print(f"seed is {seed}")
        current = int(seed)
        for i,line in enumerate(splitfile):
            if(i==0):
                seeds=line[6:].split()
                continue
            flag = 0
            for i,losts in enumerate(line.split("\n")):
                if(i!=0):
                    lost = losts.split(" ")
                    print(lost)
                    if(len(lost)>1 and flag==0):
                        if(current>=int(lost[1]) and 
                                current< (int(lost[1])+int(lost[2]))):
                            current = current-int(lost[1])+int(lost[0])
                            flag = 1
            print("---")
        sab.append(current)
    print(min(sab))

