# This is a program to calculate simple interest.
def simple_interest(p,n,r):
    """This function calculates simple interest and Amount"""
    i=(p*n*r)/100
    a=p+i
    return i,a

# Take p,n,r as input from user
p=float(input('please enter principal in INR : '))
n=int(input('please enter number of years :'))
r=float(input('please enter rate of interest in %p.a'))

# call simple interest function 
i,a=simple_interest(p,n,r)

# show the final results
print(f'Simple Interest :{i:.2f} INR')
print(f'Amount :{a:.2f} INR')
