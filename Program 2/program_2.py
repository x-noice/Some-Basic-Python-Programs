def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)

def simple_interest(principal, rate, time):
    SI = (principal * rate * time) / 100
    print("Simple interest is", SI)
  
principal = eval(input("Enter the principal amount: "))
rate = eval(input("Enter rate of interest: "))
time = eval(input("Enter time in years: " ))
compound_interest(principal,rate,time)
simple_interest(principal,rate,time)