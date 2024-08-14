# WAF to convert US.Dollar to IN.Rupees. {1 USD = 83 INR}.

usd=int(input("Enter in Dollar : "))

def USDtoINR(s):
    print(s,"USD =",usd*83,"INR")

USDtoINR(usd)