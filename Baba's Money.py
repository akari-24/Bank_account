p = float(input("what's the principle "))
r = float(input("what's the rate "))
n = int(input("How many periods "))
t = int(input("how many payments per period "))
pv = p * (pow((1 + r/100/n),n*t))

print(pv)


def compound_interest(p,r,n,t):
    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    print("Balance at the end of the period ",round(balance,2))
    print("Iterest earned is ",round(ci,2))


compound_interest(5000,10,12,5)
