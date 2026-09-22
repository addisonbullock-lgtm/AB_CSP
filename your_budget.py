# AB Your Budget.py

income = float(input("What is your monthly income: $"))

rent = float(input("What is your monthly rent/mortgage: $"))

utilities = float(input("What is your monthly utilities: $"))

groceries = float(input("What is your monthly groceries: $"))

transportation = float(input("What is your monthly transportation: $"))

# 2. Perform calculations

savings = income * 0.10  # 10% of total income

total_expenses = rent + utilities + groceries + transportation

spending_money = income - total_expenses - savings

# Calculate percentages of income

rent_percent = (rent / income) * 100

utilities_percent = (utilities / income) * 100

groceries_percent = (groceries / income) * 100

transportation_percent = (transportation / income) * 100

savings_percent = (savings / income) * 100

# 3. Display results

print(f"Your rent is $ {rent:.2f} and that is {round(rent_percent)}% of your income.")

print(f"Your utilities are $ {utilities:.2f} and that is {round(utilities_percent)}% of your income.")

print(f"Your groceries are $ {groceries:.2f} and that is {round(groceries_percent)}% of your income.")

print(f"Your transportation is $ {transportation:.2f} and that is {round(transportation_percent)}% of your income.")

print(f"You should save $ {savings:.2f} a month, that is {round(savings_percent)}% of your income.")

print(f"You have $ {spending_money:.2f} of spending money each month!")