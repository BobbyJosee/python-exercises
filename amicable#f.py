def prodiv_sum(n): #sum of proper divisors
    
    dSum = 0
    for x in range(1, n/2 + 1):
        if n % x == 0:
            dSum += x
    return dSum

def amic_sum(number):  #sum of amicable pair

    res = 0
    for x in range(4, number):
        if prodiv_sum(x) > 4:
	    temp = prodiv_sum(x)
            y = prodiv_sum(temp)	
            if x == y and prodiv_sum(x) != x:
                res += x
               
    print res

print amic_sum(10000)
