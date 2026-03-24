list1 = [1,3,4,5,7,9,8]
squared = []
for i in list1:
    squared.append(i*i)
print(squared)
evens, odds = [],[]
for n in squared:
    if n % 2== 0:
        evens.append(n)
    else:
        odds.append(n)
print(evens)
print(odds)