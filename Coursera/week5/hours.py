

hrs = input("Enter Hours : ")
rate = input('enter rate : ')
h = float(hrs)
r = float(rate)

if (h > 40):
    initial = 40 * r
    print('first 40 hours :', initial)
    extra = ((h - 40) * (r * 1.5))
    print('Extra hours: ', extra)
    pay = initial + extra
    print("pay : ", pay)
else:
    pay = h * r
print(pay)

c = 40 * 10.50
print('Manual pay', c)