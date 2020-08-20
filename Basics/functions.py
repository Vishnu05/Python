
# functions 
def add():
    # calculator
    a = int(input('Enter the value of a : '))
    b = int(input('Enter the value of b : '))

    return a + b

print('Value of two number : ', add())


# coursera def assignment 

def computepay(h,r):
    
    if ( h > 40):
        inital = 40 * r
        extra = (h - 40) * ( r * 1.5)
        pay = inital + extra
        return pay
    else:
        return h * r


h = float(input("Enter Hours:"))
r = flaot(input('enter rate'))
          
p = computepay(h, r)
print("Pay",p)
