def a(b):
    c = len(b) -1
    d = 0
    while(d<c):
        if(b[d]!=b[c]):
            return False
        d+=1
        c-=1
    return True
b =(6,7,67,67,7,6)
if(a(b)):
    print("the tuple is flip flop")
else:
    print("the tuple is not flip flop")