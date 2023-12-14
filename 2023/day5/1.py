with open("input.txt") as file:
    #parse input
    sab = []
    seeds = []
    splitfile = file.read().split("\n\n")
    for i,line in enumerate(splitfile):
        if(i==0):
            seeds=line[6:].split()
            continue

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

