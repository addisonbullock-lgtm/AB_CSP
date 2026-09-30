# AB Function
def stupid_proof(money):
    while True:
        amount= float(input(f"What is your monthly {money}: "))
        return amount
    exept:
        print("That isn't a number : (")



#Write all of your variables
income= stupid proof("income")
rent= stupid_proof("rent")
utilities= stupid_proof("utilities")
grocerise= stupid_proof("grocerise")
transportation= stupid_proof("transportation")

income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent/mortgage: "))
utilities = float(input("What is your monthly utilities: "))
groceries = float(input("What is your monthly groceries: "))
transportation = float(input("What is your monthly transportation: "))
savings= income * .1

#Write any function you are using
def calc_percent(income,bill):
    return round(bill/income *100)

#Outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent} (income,rent)% of your income.")
print(f"Your utilities is ${utilities:.2f} that is {calc_percent} (income,utilities)% of your income.")
print(f"Your income is ${income:.2f} that is {calc_percent} (income,income)% of your income.")
print(f"Your grocerise is ${grocerise:.2f} that is {calc_percent} (income,grocerise)% of your income.")
print(f"Your transportation is ${transportation:.2f} that is {calc_percent} (income,transportation)% of your income.")
