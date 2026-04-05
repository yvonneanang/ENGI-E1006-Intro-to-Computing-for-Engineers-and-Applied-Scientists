# Project 2 - Take Home 2
#submitted by Yvonne Naa Ardua Anang 

def select_meal():
    final_order = []
    while True:
        meal_choice = input("Hello would you like pizza or salad?:>>>")
        if meal_choice == "pizza":
            order = pizza()
        elif meal_choice == "salad":
            order = salad()
        elif meal_choice == "done":
            print ("Your order has been placed. Goodbye.")
            break
        final_order.append(order)
        ordered_choices = ""
        for x in range(len(final_order)):
            if x == (len(final_order) - 2):
                ordered_choices += final_order[x] + " and "
            elif x == (len(final_order) - 1):
                ordered_choices += final_order[x] + "."
            elif x != (len(final_order) - 2) and x!= (len(final_order) - 1):
                ordered_choices += final_order[x] + ", "
        placed_order = "You ordered {} Place another order or say 'done'.".format(ordered_choices)
        print (placed_order)
     

def pizza():
    pizza_choice = input("Small, medium, or large?:>>>")
    topping_choice = topping()
    string_of_topping_and_pizza_choice = "a {} pizza {}".format(pizza_choice,topping_choice)
    return string_of_topping_and_pizza_choice

def topping():
    list_of_topping_choices =[]
    count = 0
    while count < 3:
        topping_choice = input("Add a topping: pepperoni, mushrooms, spinach, or say 'done':>>>")
        if topping_choice == "done":
            break
        list_of_topping_choices.append(topping_choice)
        count+=1

    string_of_topping_choices = ""
    if len(list_of_topping_choices) == 3:
        string_of_topping_choices = "with {}, {} and {}".format(list_of_topping_choices[0], list_of_topping_choices[1], list_of_topping_choices[2])
    elif len(list_of_topping_choices) == 2:
        string_of_topping_choices = "with {} and {}".format(list_of_topping_choices[0], list_of_topping_choices[1])
    elif len(list_of_topping_choices) == 1:
        string_of_topping_choices = "with {}".format(list_of_topping_choices[0])
    
    return string_of_topping_choices

def salad():
    salad_choice = input("Would you like a garden salad or greek salad?:>>>")
    dressing_choice = dressing()
    string_of_dressing_and_salad_choice = "a {} salad {}".format(salad_choice, dressing_choice)
    return string_of_dressing_and_salad_choice

def dressing():
    dressing_choice = input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon.:>>>")
    string_of_dressing_choice = "with {} dressing".format(dressing_choice)
    return string_of_dressing_choice
select_meal()      
