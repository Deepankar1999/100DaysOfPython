sum=0

for n in range(101):
    
    if n%2 ==0:
        sum+=n
print(sum)

#Alternative
asum=0
for n in range(2,101,2):
    asum+=n
print(asum)