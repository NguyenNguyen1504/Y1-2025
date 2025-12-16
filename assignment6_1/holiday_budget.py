def create_budget():
    print("Create budget / format: category,spending_limit / press enter to continue:")
    budget = {}
    text = input()
    while text != "":
        input_details = text.split(',')
        category, limit = input_details[0], input_details[1]
        limit = float(limit)

        if category == "":
            print("The category cannot be empty.")
        elif limit < 0:
            print("The limit cannot be negative.")
        else:
            # if the category is already in the budget, print an error
            # otherwise, add it to the budget
            if category in budget:
                print("The category is already in the budget.")
            else:
                budget[category] = limit

        text = input()
    return budget


def add_expenses(budget):
    print("Add expenses / format: category,amount_paid / press enter to continue:")
    text = input()
    while text != "":
        input_details = text.split(',')
        category, amount = input_details[0], input_details[1]
        amount = float(amount)
        if amount <= 0:
            print("The amount must be positive.")
        else:
            if category not in budget:
                print("The category is not in the budget.")
            else:
                old_budget = budget[category]
                budget[category] -= amount
                print(f"{category}: {old_budget:6.2f}e -> {budget[category]:6.2f}e")
                if amount > budget[category]:
                    print("You have exceeded your limit!")

        # if the category is not in the budget, print an error
        # otherwise, decrease the category limit by the given amount

        text = input()


def print_budget(budget):
    print("Current budget / amount of money left in each category:")
    # code:
    # print all categories by iterating through the budget
    for category in budget:
        print(f"{category:30s}| {budget[category]:6.2f}e")

def main():
    print("Holiday Budget", '-' * 30)
    budget = create_budget()
    add_expenses(budget)
    print_budget(budget)

main()