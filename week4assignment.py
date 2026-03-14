def canteen_budget(days, meal_plan, extra_snacks = 0, sibling_discount = False):
    
    if meal_plan == "basic":
        daily_cost = 15000
       
    if meal_plan == "standard":
        daily_cost = 25000

    if meal_plan == "premium":
        daily_cost = 40000

    total = daily_cost * days + extra_snacks * 5000

    if days >= 20:
        total = total * 0.95

    if sibling_discount == True:
        total = total * 0.88
    return total
print(canteen_budget(10, "basic"))
        
         
print(canteen_budget(22, "standard", extra_snacks=5))
# 546250

print(canteen_budget(20, "premium", sibling_discount=True))
# 668800

print(canteen_budget(15, "basic", extra_snacks=10, sibling_discount=True))
# 242000
