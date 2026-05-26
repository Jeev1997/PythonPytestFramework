

amount = 400
discount = 0

if amount >= 10000:
    discount = amount * (20/100)
    print(f"the discount is {discount}")

elif amount >5000 and amount < 10000:
    discount = amount * (10/100)
    print(f"the elif discount is {discount}")

elif amount >=1000 and amount <= 5000:
    discount = amount * (5/100)
    print(f"the discount is {discount}")
else :
    print("the discount is not available")
