your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

if your_total > partner_total:
    spender = "You"
elif your_total < partner_total:
    spender = "Your partner"
else:
    spender = "Both of you spent the same amount"

category_differences = {key: abs(your_expenses[key] - partner_expenses[key]) for key in your_expenses}
largest_difference_category = max(category_differences, key=category_differences.get)
largest_difference_value = category_differences[largest_difference_category]

print(f"Your total expenses: {your_total}")
print(f"Your partner's total expenses: {partner_total}")
print(f"{spender} spent more overall.")
print(f"The biggest spending difference was in '{largest_difference_category}' with a difference of {largest_difference_value}.")
