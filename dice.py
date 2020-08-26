from random import choices
nrolls=10000
total=0
ndice=3
for i in range(nrolls):
    dice=choices(range(1,7),k=ndice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
print("Average roll=",total/nrolls)

#ndice=2 Average roll: 6.9956
#ndice=3 Average roll: 8.4862
# 8.4862 - 6.9956 = 1.4906 increase in the average just by adding another dice
#If my friend added one point to my two die, the game would not be fair because the difference in the average of the roll is ~1.5 which is greater than 1.