import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()

        if choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich['ingredients']):
                print(f"The cost of a {choice} sandwich is ${sandwich['cost']}.")
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(choice, sandwich['ingredients'])
            else:
                print("Sorry, we do not have enough ingredients to make that sandwich.")
        elif choice == "off":
            is_on = False
        else:
            print("Invalid choice. Please choose small, medium, or large.")

if __name__=="__main__":
    main()
