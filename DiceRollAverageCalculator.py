count=10000
a=list()
for i in range(count):
    ans=random.randint(1,6)
    n=1
    while ans!=6:
        ans=random.randint(1,6)
        n+=1
    a.append(n)
print(a)
print(sum(a)/len(a))
