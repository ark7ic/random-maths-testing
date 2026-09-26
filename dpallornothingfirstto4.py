import numpy as np
valarr = np.empty((5,5))
#array of money we should have at each point
valarr[:,4] = 200
#all or nothing so shld have 200 if our team wins the set (first to 4)
valarr[4,:] = 0 
#all or nothing so 0
betarr = np.empty((4,4))
for i in range(3,-1,-1):
    for j in range(3,-1,-1):
        valarr[i,j] = 0.5*(valarr[i+1,j] + valarr[i,j+1])
       #if my team wins here, i have val[i+1], if they lose i have val[j+1]. for these to be the result of a bet, 
       #my current value has to be the average of these too
        betarr[i,j] = 0.5*(valarr[i,j+1] - valarr[i+1,j])
      #my bet is half the difference of the win/lose scenarios
print(valarr, betarr)
