def sumAll():
    values = []
    total = 0
    for i in range(0,1000,3):
        values.append(i)
    for j in range(0,1000,5):
        if not(j in values):
            values.append(j)
    for k in range(0,len(values)):
        total += int(values[k])
    return total
print(sumAll())
