"""
pv = p * (pow((1 + r/100/n),n * t))

print (pv) 

"""
def compound_interest():
  p = float(input("What's the principle? "))
  r = float(input("What's the rate? "))
  n = int(input("How many periods? "))
  t = int(input("How many payments per period? "))


  balance = p * (pow((1 + r/100/n),n*t))
  ci = balance - p
  print("Your balance at the end of the period will be $ ", round(balance,2), "\n")


  print("You earned $", round(ci,2), "during the 1 year period.")


  roi = (ci/balance) * 100
  print("This is", round(roi,2),"% return on investment.")

compound_interest()

"""
interst = G * balance 

12.68 = G * 112.68

12.68/112.68 = G * 112.68/112.68

0.112555 = G

0.11255 * 100 = G

11.255 = G and/or G = 11.26%

roi = return on investment = 11.26% 
"""
