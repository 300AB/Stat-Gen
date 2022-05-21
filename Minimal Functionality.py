import random

def Stat(min=0):
    rr = random.randint
    r1 = rr(1,6)
    r2 = rr(1,6)
    r3 = rr(1,6)
    if min != 0:
        print("debug output:",r1,"+",r2,"+",r3, "=", r1+r2+r3)
    return r1+r2+r3

#char = how many stat rolls
char = 10

#set each Stat() to Stat(1) to debug and see all d6
for i in range(char+1): 
    print(Stat(),Stat(),Stat(),Stat(),Stat(),Stat(),)