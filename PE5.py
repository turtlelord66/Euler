def smallestMultiple():
    answer = 0
    for i in range(20,10000000000,20):
        if all([i % j == 0 for j in range(1,21)]):
            answer = i
            return answer
print(smallestMultiple())


