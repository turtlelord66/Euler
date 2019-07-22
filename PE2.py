def sumAll():
    sequence = [1,2]
    evenSequence = [2]
    x = 0
    total = 0
    for i in range(0,100000000):
        x = sequence[i] + sequence[(i+1)]
        if x > 4000000:
            break
        sequence.append(x)
        if (x % 2) == 0:
            evenSequence.append(x)
    for j in range(0,len(evenSequence)):
        total += evenSequence[j]
    return total
print(sumAll())
                   
