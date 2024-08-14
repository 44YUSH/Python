# WAF to convert US.Dollar to IN.Rupees. {1 USD = 83 INR}.

usd=int(input("Enter in Dollar : "))

def USDtoINR(s):
    print("USD value : ",s)
    print("INR value : ",usd*83)

USDtoINR(usd)