a = {"Codingal":2,"is":2,"best":2,"for":2,"coding":1}
k = 2
res = 0
for key in a:
    if a[key] == k:
        res = res+1
print("frequency of K is:"+str(res))