from random import choices
ntrials = 1000000
limit = 1000
count = 0
for i in range(ntrials):
    rand = choices(range(1 ,limit+1) , k=3)
    if rand[0]+rand[1]<=rand[2]:
        count = count+1
print("Fraction=", count/ntrials)

#The answers are not the same because we are sampling random numbers.
#Yes, increasing the number of trials takes the simulation more time to complete the command.
#No, the percentage does not change. You essentially get the same value of 0.167.