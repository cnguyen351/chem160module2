from random import choice
trials=1000
steps=10000
gothome=0
for i in range(trials):
    point=0
    for step in range(steps):
        point+=choice((-1,1))
        if point==0:
            gothome+=1
            break
print("Fraction that got home=",gothome/trials)

#My result is Fraction=1.0. So the random walker always ends up home.
#My result is Fraction=0.993. My result was affected. by 0.007.