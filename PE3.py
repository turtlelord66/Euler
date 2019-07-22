def maxPrimeFactor(number):
    allPrimeFactors = []
    i = 2
    biggestPrimeFactor = 0
    while number > 1:
        while number % i == 0:
            allPrimeFactors.append(i)
            number /= i
        i = i + 1
    for j in range(0,len(allPrimeFactors)):
        if not(j == 0):
          if allPrimeFactors[(j-1)] < allPrimeFactors[j]:
              biggestPrimeFactor = allPrimeFactors[j]
    return biggestPrimeFactor
print(maxPrimeFactor(600851475143))
