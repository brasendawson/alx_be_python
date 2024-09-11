monthy_income = int(input("Enter your monthly income: "))
monthy_expenses = int(input("Enter your total monthly expenses: "))

monthy_savings = monthy_income - monthy_expenses
print("Your Monthly savings are $",monthy_savings,".")

projected_savings = (monthy_savings * 12 + (monthy_savings) * 12 * 0.05)
print("Projected savings after one year, with interest, is: $", projected_savings)