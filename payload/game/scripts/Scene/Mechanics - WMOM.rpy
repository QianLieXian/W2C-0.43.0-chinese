# -----------------------------------------------------------------------------------------------
label wmom_checkfridge: # Check Home Lunch
# -----------------------------------------------------------------------------------------------
    python:
        for buceta in inventory_fridge:
            if buceta not in wmom_item: # WMOM detects an item she didn't know
                wmom_item.append(buceta) # WMOM know new item
                wmom_love += round(xereca["valu"] / 50, 2)
                if not "HERO_2_Fridge" in wmom_know:
                    wmom_know.append("HERO_2_Fridge")
                    msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] must have noticed that you've been helping out around the house."))
    return

# -----------------------------------------------------------------------------------------------
label wmom_autocook_check: # Check Ingredients
# -----------------------------------------------------------------------------------------------
    if (CountItem_Inventory("Eat_Farm_Bread", inventory_fridge) >= 2) and (CountItem_Inventory("Eat_Farm_Egg", inventory_fridge) >= 2):
        $ wmom_act[1] = "cooking Eat_Snack_SandwichEgg"
        if not "is_cooking" in wmom_know:
            $ wmom_know.append("is_cooking")
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] is preparing a breakfast"))

    elif (CountItem_Inventory("Eat_Farm_Bread", inventory_fridge) >= 2) and (CountItem_Inventory("Eat_Farm_Cheese", inventory_fridge) >= 2) and (CountItem_Inventory("Eat_Meat_Ham", inventory_fridge) >= 2):
        $ wmom_act[1] = "cooking Eat_Snack_SandwichCheeseHam"
        if not "is_cooking" in wmom_know:
            $ wmom_know.append("is_cooking")
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] is preparing a breakfast"))

    elif CountItem_Inventory("Eat_Farm_Egg", inventory_fridge) >= 2:
        $ wmom_act[1] = "cooking Eat_Meal_EggFried"
        if not "is_cooking" in wmom_know:
            $ wmom_know.append("is_cooking")
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] is preparing a breakfast"))
        #$ AddItem_Inventory("Eat_Farm_Egg", 2, (4, 5), wmom_item)

    else:
        if not "is_shopping" in wmom_know:
            $ wmom_know.append("is_shopping")
            $ msg.msg(renpy.translate_string("[C_Nam][fnamewmom][C_Off] went shopping"))
        $ wmom_act[1] = "shopping"

    return

# -----------------------------------------------------------------------------------------------
label wmom_autocook_cook(lunch): # Serving
# -----------------------------------------------------------------------------------------------
    if wmom_act[1] == "cooking Eat_Snack_SandwichEgg":
        $ msg.msg(renpy.store._zh_format_display("[C_Nam][fnamewmom][C_Off] made [C_Dat]Egg Sandwich[C_Off] for ", [])+renpy.translate_string(str(str(lunch))))
        $ AddItem_Inventory("Eat_Snack_SandwichEgg", 2, (4, 5), inventory_home_table)

    elif wmom_act[1] == "cooking Eat_Snack_SandwichCheeseHam":
        $ msg.msg(renpy.store._zh_format_display("[C_Nam][fnamewmom][C_Off] made [C_Dat]Ham Sandwich[C_Off] for ", [])+renpy.translate_string(str(str(lunch))))
        $ AddItem_Inventory("Eat_Snack_SandwichCheeseHam", 2, (4, 5), inventory_home_table)

    elif wmom_act[1] == "cooking Eat_Meal_EggFried":
        $ msg.msg(renpy.store._zh_format_display("[C_Nam][fnamewmom][C_Off] made [C_Dat]Fried Egg[C_Off] for ", [])+renpy.translate_string(str(str(lunch))))
        $ AddItem_Inventory("Eat_Meal_EggFried", 2, (4, 5), inventory_home_table)

    elif wmom_act[1] == "shopping":
        $ AddItem_Inventory("Eat_Veg_Apple", 2, inventory_id=inventory_home_table)
        $ AddItem_Inventory("Eat_Veg_Banana", 2, inventory_id=inventory_home_table)
        $ msg.msg(renpy.store._zh_format_display("[C_Nam][fnamewmom][C_Off] bought [C_Dat]apples[C_Off] for ", [])+renpy.translate_string(str(str(lunch))))
        $ msg.msg(renpy.store._zh_format_display("[C_Nam][fnamewmom][C_Off] bought [C_Dat]bananas[C_Off] for ", [])+renpy.translate_string(str(str(lunch))))

    if gametimeweek != "Sunday":
        $ wmom_act[1] = "working"
    else:
        $ wmom_act[1] = "cleaning"

    return

    # To Save
    if (gametimehour == 7 and gametimemin <= 50): # Breakfast at 7:00 - 7:50
        $ gametimeeat = "breakfast"
    elif ((gametimehour == 11 and gametimemin >= 30) and (gametimehour == 12 and gametimemin < 30)): # Lunch at 11:30 - 12:29
        $ gametimeeat = "lunch"
    elif ((gametimehour == 17 and gametimemin >= 30) and (gametimehour == 18 and gametimemin < 30)): # Dinner at 17:30 - 18:29
        $ gametimeeat = "dinner"
