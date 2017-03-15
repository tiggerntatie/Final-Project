MAX = int(input("How many primes should I count? "))
i = 0
a = 2
primelist = [1]
    
while i !=MAX:
    b = 0
    for x in primelist:
        if int(a)%int(x) == 0:
            b += 1
    if b == 1:
        primelist.append(a)
        a += 1
        i+=1
    else:              
        a+=1
print(primelist[len(primelist])
