from random import choice
dim=3
trials=100
steps=10000
gothome=0
for i in range(trials):
    point=[0]*dim
    for step in range(steps):
        for j in range(dim):
            point[j]+=choice((-1,1))
        if point.count(0)==dim:
            gothome+=1
            break
print("Fraction that got home=%f in %d dims" % (gothome/trials,dim))

#The result was Fraction= 0.71 in 2 dimension. The walker made it home 71% of the time which is very often.
#The result was Fraction=0.21 in 3 dimension. The walker made it home 21% of the time which is not very often.