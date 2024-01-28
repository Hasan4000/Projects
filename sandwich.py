import pyinputplus as pyip

bread = pyip.inputMenu(choices=["wheat", "White", "Sourdough"], prompt="\nWhat type of bread do want?\nwheat: 5, White: 7, Sourdough: 6\n\n", numbered=True,)

meat = pyip.inputMenu(choices=["Lamb", "Chicken", "Turkey"], prompt="\nWhat type of meat do want?\nLamb: 20, Chicken: 15, Turkey: 20\n\n", numbered=True)

ingrediants = [bread, meat]

if pyip.inputYesNo(prompt="\nDo you want cheese (yes/no): ") == "yes":
    cheese = pyip.inputMenu(choices=["Cheddar", "Mozzarella", "Swiss"], prompt="\nWhat type of cheese do want?\nCheddar: 7, Mozzarella: 8, Swiss:10\n\n", numbered=True)
    ingrediants.append(cheese)

if pyip.inputYesNo(prompt="\nDo you want any ketchap, mayo, mustard, tomato (yes/no): ") == "yes":
    additions = pyip.inputMenu(choices=["ketchap", "mayo", "mustard", "tomato"], prompt="\nWhat do want?\ketchap: 2, mayo: 2, mustard: 3, tomato: 3\n\n", numbered=True)
    ingrediants.append(additions)


prices = {"wheat": 5, "White": 7, "Sourdough": 6,
          "Lamb": 20, "Chicken": 15, "Turkey": 20,
          "Cheddar": 7, "Mozzarella": 8, "Swiss":10,
          "ketchap": 2, "mayo": 2, "mustard": 3, "tomato": 3}

cost = 0
for i in ingrediants:
    cost += prices[i]
#cost = sum(prices[i] for i in ingredients)

print(f"Your sandwiche cost: {cost} L.E.", "Have a nice day! :)\n")

#put \n to the phrases