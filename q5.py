for x in range(0,1000000020, 20):
    total = 0
    if x !=0:
        
        for y in range(19,2,-1):
            
            if x%y!=0:
                break
            else:
                total += 1
    if total >=17:
        print(x)
        break
