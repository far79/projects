total_runs = 0
wickets = 0
overs = 0
balls = 0

update = input("Press enter to continue:")

while (update == "") or (update == "enter"):
    if balls == 6:
        overs+=1
        balls = 0
    print(overs,".",balls,sep="")
    

    runs = input("enter run on this ball or type 'w' for wicket or 'wide' for wide ball:")

    if (runs == "w"):
        wickets+=1
        balls +=1
        print("total wickets are:",wickets)

    elif (runs == "wide"):
        total_runs +=1
        print("total runs:",total_runs)

    else:
        runs = int(runs)
        total_runs +=runs 
        print("total runs:",total_runs)
        balls += 1


