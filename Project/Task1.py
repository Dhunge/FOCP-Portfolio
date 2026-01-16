import math

def ask_price(prompt):
    while True:
        try:
            p = float(input(prompt))
            if p > 0: return p
        except ValueError:
            pass
        print("Please enter a valid price!")

print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================\n")

# 1. Get the 4 prices into separate variables
p1 = ask_price("Enter Price of Pizza #1: ")
p2 = ask_price("Enter Price of Pizza #2: ")
p3 = ask_price("Enter Price of Pizza #3: ")
p4 = ask_price("Enter Price of Pizza #4: ")

# 2. Add them all up
full_total = p1 + p2 + p3 + p4

# 3. Find the cheapest one
cheapest = min(p1, p2, p3, p4)

# 4. Calculate final results
final_cost = full_total - cheapest
percentage = math.ceil((cheapest / full_total) * 100)

print()
print(f"Order Total is \u00A3{final_cost:.2f}, a fabulous discount of {percentage}%!")