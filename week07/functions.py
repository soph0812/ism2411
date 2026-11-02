# --- Self-Assessment ---
# 1. In Exercise 5, the first bug I spotted was the missing colon in the for loop. I found it from the traceback because Python pointed to the exact line 
# and said "expected ':'". This shows that I am getting better at using error messages to find where a problem is.
# 2. apply_discount(price, tier) takes the price of an item and the customer's discount tier. It checks if the tier is gold, silver, bronze, or none, then 
# returns the price after the correct discount is applied. A colleague could use it without reading the body as long as they know the price and tier are 
# the two inputs.
# 3. AI Disclosure: I used AI only for Exercise 5 to help explain the error message and understand what the bugs meant. The AI helped me understand the 
# errors, but I still made the fixes myself.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
tax1= calculate_tax(100, 0.07)
tax2= calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1}")
print(f"Tax on $250 at 8%: ${tax2}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
rate=0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Order: ${price}, Tier: {tier}, Final Price: ${total:.2f}")

# --- Exercise 5 ---
# --- AI Explainer ---
# Bug 1: The for loop was missing a colon after "sales".
# Bug 2: total = sale replaced the previous total instead of adding each sale.
# Bug 3: The while loop used <= len(sales), which caused it to try to access an index that does not exist.
sales = [120, 80, 250, 175, 90]
# Fixed Bug 2
total = 0
for sale in sales: 
    total = total + sale # I changed total = sale to total = total + sale so each sale is added to the running total.
print(f"Total: ${total}")
# Fixed Bug 1
count = 0
for sale in sales: # I added the colon because Python needs one at the end of a for loop.
    count += 1
print(f"Count: {count}")
# Fixed Bug 3
i = 0
while i < len(sales): # I changed <= to < so the loop stops before trying to access an index that does not exist.
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100   # global variable
def double_it():
    x = 999   # local variable
    return x * 2

print(x)
print(double_it())
print(x)
# The x inside the function is a local variable, so it is separate from the global x outside the function. Changing the local x does not change the global x.