def simple_interest(p,n,r):
    print('The principal is', p)
    print('The time period is', n)
    print('The rate of interest is',r)
    si = (p * n * r)/100
    print('The Simple Interest is', si)
    return si
# Driver code
simple_interest(10,20,30)
