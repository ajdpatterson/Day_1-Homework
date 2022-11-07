meal_1 = "Steak surprise"
meal_2 = "Grapefruit Supreme"
meal_1_cost = 10.99
meal_2_cost = 14.09

meal_selection_text = meal_1 + " and " + meal_2
meal_cost_sum = meal_1_cost + meal_2_cost
print("You have chosen " + meal_selection_text)
print(f"25% discount applied! You have saved £{meal_cost_sum * 0.25}")
print(f"Please pay £{meal_cost_sum * 0.75}")