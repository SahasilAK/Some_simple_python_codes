print("Welcome to the tip calculator")

total = float(input("What was the total bill??\t"))
tiper = int(input("What percentage would u like to tip 10, 12 or  15??\t"))
split = int(input("how many people to split the bill?\t"))



if tiper == 10:
    tips = total*(10/100)
    totip = total + tips
elif tiper == 12:
    tips = total*(12/100)
    totip = total + tips
elif tiper == 15:
    tips = total*(15/100)
    totip = total + tips

cash = totip/split
pay = round(cash, 2)
print(f"Each person should pay :\t ${pay}")
