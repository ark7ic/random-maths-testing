import numpy as np
val2arr = np.empty((20))
#if u have X money, then if u roll again, u end with 0 with prob 1/6 (roll 6), and prob 1/6 for X+i from i from 1 to 5
#find that we have expected gain for X leq 15. so, stop rolling once hit 15
#then, max possible amount to end at is 19 (if u rolled at 14 and scored a 5), so initialise a len 20 vector
val2arr[-5:] = np.arange(15,20)
#for values 15,16,17,18,19, we dont roll again, so the expected payoff is just that number
for j in range (14,-1,-1):
    val2arr[j] = 1/6 * (val2arr[j+1] + val2arr[j+2] + val2arr[j+3] + val2arr[j+4] + val2arr[j+5])
  #expected payoff for the previous vals
print(val2arr)
#we technically only care abt val2arr[0] but this is instructive
