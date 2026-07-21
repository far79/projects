total_runs = 0
wickets = 0
overs = 0
balls = 1

update = input("Press enter to continue:")

while (update == "") or (update == "enter"):

    runs = input("enter run on this ball or type 'w' for wicket or 'wide' for wide ball:")

    # if (runs == "no ball"):
    #     pass

    # else:
    #     if balls == 6:
    #         overs+=1
    #         balls = 0
    #     print(overs,".",balls,sep="")
    
    if balls == 6:
        overs+=1
        balls = 0
    print(overs,".",balls,sep="")

    if (runs == "no ball"):
        print("free hit")
        print(overs,".",balls,"f",sep="")
    

    elif (runs == "w"):
        wickets+=1
        balls +=1
        print("total wickets are:",wickets)

    elif (runs == "wide"):
        total_runs +=1
        print("total runs:",total_runs-1)

    else:
        runs = int(runs)
        total_runs +=runs 
        balls += 1
        print("total runs:",total_runs)
        



