# ==================================================
# Class
# ==================================================
init python:
    class Item:
        def __init__(self, item_id, quality=None):
            self.item_id = item_id # "Eat_Egg"
            self._resolve_data()

            self.quality = quality # Quality (0 = terrible, 100 = perfect)
            self.effect = {} # Effects from cooking

        def _resolve_data(self):
            # Re-attach the item_data dict for this item_id. Lives in init state, never pickled, so function references inside cook_steps[*]['mg'] remain picklable (functions are saved by name reference).
            if self.item_id in item_data:
                self.data = item_data[self.item_id]
            elif self.item_id in item_id_migrations:
                self.item_id = item_id_migrations[self.item_id]
                self.data = item_data[self.item_id]
            else:
                renpy.log("ERROR: Item '{}' not found in item_data".format(self.item_id))
                self.data = {
                    "icon": None,
                    "name": "Unknown Item",
                    "valu": 0,
                    "cons": False,
                    "type": ["unknown"],
                    "tags": [],
                    "info": "This item doesn't exist in the database.",
                    "fx_a": "None",
                    "fx_i": "None",
                }

        def __getstate__(self):
            # Skip .data — it references the init-time item_data dict.
            # The pickled Item only carries identity; data is re-resolved on
            # load via __setstate__. This keeps save files small and ensures
            # item_data updates apply to old saves.
            state = self.__dict__.copy()
            state.pop("data", None)
            return state

        def __setstate__(self, state):
            self.__dict__.update(state)
            self._resolve_data()

# ==================================================
# Item Functions
# ==================================================
init python:

    def HasItem_Inventory(item_id, inventory_id=None):
        """Check if item with this ID exists in inventory"""
        if inventory_id is None:
            inventory_id = inventory
        
        return any(item.item_id == item_id for item in inventory_id)


# --------------------------------------------------
# Add item to inventory (creates Item instance)
# --------------------------------------------------
    def AddItem_Inventory(item_id, item_count=1, item_quality=None, inventory_id=None):
        """Add an item instance to inventory"""

        if inventory_id is None:
            inventory_id = inventory  # player inventory as default

        added_items = []
        for i in range(item_count):
            # Check if quality is a tuple/list (min, max) for random
            if isinstance(item_quality, (tuple, list)) and len(item_quality) == 2:
                quality = renpy.random.randint(item_quality[0], item_quality[1])
            else:
                quality = item_quality
            
            new_item = Item(item_id, quality)
            inventory_id.append(new_item)
            added_items.append(new_item)
        return added_items

# --------------------------------------------------
# Remove item from inventory (finds matching instance)
# --------------------------------------------------
    def RemItem_Inventory(item_instance, inventory_id=None):
        """Remove specific item instance from inventory"""

        if inventory_id is None:
            inventory_id = inventory  # player inventory as default

        if item_instance in inventory_id:
            inventory_id.remove(item_instance)
            return True
        return False

# --------------------------------------------------
# Count items by ID
# --------------------------------------------------
    def CountItem_Inventory(item_id=None, inventory_id=None):
        """
        Count how many items with this ID exist in inventory
        
        Args:
            item_id: The item ID to search for
            inventory_id: The inventory to search in (can be list of objects or list of strings)
        """
        
        if inventory_id is None:
            inventory_id = inventory  # player inventory as default
        
        if item_id is None:
            return 0
        
        return sum(
            1 for item in inventory_id 
            if (hasattr(item, 'item_id') and item.item_id == item_id) or (isinstance(item, str) and item == item_id)
        )

# --------------------------------------------------
# Get first item by ID (useful for consumption/usage)
# --------------------------------------------------
    def GetItem_Inventory(item_id, inventory_id=None):
        """Get first item instance matching this ID from inventory"""

        if inventory_id is None:
            inventory_id = inventory  # player inventory as default
            
        for item in inventory_id:
            if item.item_id == item_id:
                return item
        return None

# --------------------------------------------------
# Compare item type in 2 inventories
# --------------------------------------------------
    def CompareItem_Type(item_type, inventory_source, inventory_target):
        """Check if source inventory has items of specified type that exist in target but not in table"""
        for target_item in inventory_target:
            # Extract item_id (handle both Item objects and strings)
            target_item_id = target_item.item_id if hasattr(target_item, 'item_id') else target_item
            
            # Get item data from string ID
            target_data = item_data[target_item_id]
            
            # Check if item has the required type
            if item_type in target_data["type"]:
                # Check if this item type is in source inventory
                item_in_source = any(item.item_id == target_item_id for item in inventory_source)
                # Check if this item is NOT on table
                item_not_on_table = not any(item.item_id == target_item_id for item in inventory_table)
                # If item is in source but not on table, return True
                if item_in_source and item_not_on_table:
                    return True
        return False

# --------------------------------------------------
# Get ingredient list for recipe in an inventory
# --------------------------------------------------
    def GetRecipe_List(item_id, inventory_id, item_count=1):
        """Transform inventory into list of required ingredients multiplied by item_count"""
        recipe = item_data[item_id]
        
        # Clear the inventory
        inventory_id[:] = []
        
        # Add tools (only once, not multiplied)
        if "data" in recipe and "cook_tool" in recipe["data"]:
            for tool_id in recipe["data"]["cook_tool"]:
                # Migrate old IDs
                if tool_id in item_id_migrations:
                    tool_id = item_id_migrations[tool_id]
                inventory_id.append(tool_id)
        
        # Add required ingredients (multiplied by item_count)
        if "data" in recipe and "cook_ingn" in recipe["data"]:
            for ingn_id in recipe["data"]["cook_ingn"]:
                # Migrate old IDs
                if ingn_id in item_id_migrations:
                    ingn_id = item_id_migrations[ingn_id]
                for i in range(item_count):
                    inventory_id.append(ingn_id)
        
        # Add optional ingredients (multiplied by item_count)
        if "data" in recipe and "cook_ingo" in recipe["data"]:
            for ingo_id in recipe["data"]["cook_ingo"]:
                # Migrate old IDs
                if ingo_id in item_id_migrations:
                    ingo_id = item_id_migrations[ingo_id]
                for i in range(item_count):
                    inventory_id.append(ingo_id)
        
        return inventory_id

# --------------------------------------------------
# Gifting
# --------------------------------------------------
    def GiveItem_Character(char_id, char_bonus=0):
        """
        Universal gift system for all characters
        
        Args:
            char_id: Character ID (e.g., "wdel", "wgal", "wsis")
            char_bonus: Bonus points per matching tag (default: 0, so base is 5)
        
        Returns:
            "Accept": Gift was accepted and loved
            "Reject": Gift was rejected (0% match)
            "Already": Character already has this item
        """
        # Get character data dynamically
        char_name = getattr(store, f"fname{char_id}")
        char_item_list = getattr(store, f"{char_id}_item")
        char_love_tags = getattr(store, f"{char_id}_item_love")
        
        # Check if character already has this item
        if any(item.item_id == a_item_3.item_id for item in char_item_list):
            msg.msg(renpy.store._zh_format_display("[C_Nam]{char_name}[C_Off] already has this item.", [('{char_name}', format(char_name, ''))]))
            return "Already"

        # Calculate tag matches
        match_score = 0
        base_points = 5
        points_per_tag = base_points + char_bonus  # 5 for normal, 7 for WGAL
        
        for tag in char_love_tags:
            if tag in a_item_4:
                match_score += points_per_tag
        
        if match_score >= 1:
            # Calculate love gain
            add_stat(char_id, "love", match_score)
            
            # Calculate match percentage
            match_percent = min(100, match_score * 5)
            store.gift_match_percent = match_percent
            msg.msg(renpy.store._zh_format_display("You gave a [C_Dat]{a_item_1}[C_Off] to [C_Nam]{char_name}[C_Off]. It matches [C_Pos]{match_percent}%[C_Off] their likes.", [('{a_item_1}', format(a_item_1, '')), ('{char_name}', format(char_name, '')), ('{match_percent}', format(match_percent, ''))]))
            
            # Transfer item
            char_item_list.append(a_item_3)
            store.inventory.remove(a_item_3)
            
            return "Accept"
        else:
            msg.msg(renpy.store._zh_format_display("[C_Nam]{char_name}[C_Off] didn't accept [C_Dat]{a_item_1}[C_Off]. It matches [C_Neg]0%[C_Off] their likes.", [('{char_name}', format(char_name, '')), ('{a_item_1}', format(a_item_1, ''))]))
            return "Reject"

# --------------------------------------------------
# Check Ingredients for Recipe
# --------------------------------------------------
    def CheckIng_Recipe(recipe_id, recipe_count=1, inventory_id=None):
        """
        Check if we can cook X quantities of a recipe with available ingredients
        
        Args:
            recipe_id: The recipe item_id
            recipe_count: How many times we want to cook it (default: 1)
            inventory_id: Which inventory to check (default: inventory_fridge)
        
        Returns: dict with result
        {
            'can_cook': True/False,
            'max_quantity': int (max we can make),
            'missing': [] (list of missing items),
            'has_optional': True/False (if optional ingredients available)
        }
        """
        if inventory_id is None:
            inventory_id = inventory_fridge
        
        recipe = item_data[recipe_id]
        
        # Check if recipe has cooking data
        if "data" not in recipe:
            return {'can_cook': False, 'max_quantity': 0, 'missing': ['No recipe data']}
        
        recipe_data = recipe["data"]
        missing_items = []
        
        # Check required tools
        if "cook_tool" in recipe_data:
            for tool_id in recipe_data["cook_tool"]:
                if CountItem_Inventory(tool_id, inventory_id) < 1:
                    missing_items.append(tool_id)
        
        # Check required ingredients (must have ALL)
        max_possible = 999
        if "cook_ingn" in recipe_data:
            for ingn_id in recipe_data["cook_ingn"]:
                available = CountItem_Inventory(ingn_id, inventory_id)
                max_possible = min(max_possible, available)
                if available < recipe_count:
                    missing_items.append(ingn_id)
        
        # Check optional ingredients (doesn't block cooking, but tracked)
        has_optional = True
        if "cook_ingo" in recipe_data:
            for ingo_id in recipe_data["cook_ingo"]:
                available = CountItem_Inventory(ingo_id, inventory_id)
                if available < recipe_count:
                    has_optional = False
        
        # Return results
        if len(missing_items) > 0:
            return {
                'can_cook': False,
                'max_quantity': max_possible,
                'missing': missing_items,
                'has_optional': has_optional
            }
        else:
            return {
                'can_cook': True,
                'max_quantity': max_possible,
                'missing': [],
                'has_optional': has_optional
            }


# ==================================================
# Item ID Migrations (for save compatibility)
# ==================================================
init python:
    item_id_migrations = {
        # "Old_Item_Name": "New_Item_Name",
        "Ingredient_Salt": "Ingredient_Cook_Salt",
    }

# ==================================================
# Cooking Minigame Calculation Functions
# ==================================================
# These functions replace lambdas in item_data to allow save compatibility (lambdas cannot be pickled, causing save errors)
init python:
    # Physical stat scaling functions
    def calc_phy_agi_bonus(c=None):
        """Calculate physical agility bonus for balance minigame"""
        return 1.0 + perk_phy_agi * 0.02

    def calc_phy_str_bonus(c=None):
        """Calculate physical strength bonus for tug-of-war minigame"""
        return 1.0 + perk_phy_str * 0.50

    # Cooking skill timer functions (for precision minigame)
    def calc_cook_timer_green(c=None):
        """Calculate green zone timer based on cooking skill"""
        return int(60 * (1.0 + (perk_skl_cok * 1.5)))

    def calc_cook_timer_yellow(c=None):
        """Calculate yellow zone timer based on cooking skill"""
        return int(180 * (1.0 + (perk_skl_cok * 1.5)))

    def calc_cook_timer_orange(c=None):
        """Calculate orange zone timer based on cooking skill"""
        return int(300 * (1.0 + (perk_skl_cok * 1.5)))

    # Cooking skill speed functions
    def calc_cook_time_pass(c=None):
        """Calculate time passage speed based on cooking skill (for sequence minigame)"""
        return 1.0 / (1 + (perk_skl_cok * 1))

    def calc_cook_hold_time(c=None):
        """Calculate hold time based on cooking skill (for balance minigame)"""
        return 5 / (1 + (perk_skl_cok * 2))

# ==================================================
# Renamed item ids — old id : new id
# ==================================================
# Item ids are SAVED: they sit in `inventory`, `inventory_fridge`, `inventory_home_table`, `item_cart`, `item_sale` and every `<char>_item` list. Renaming one therefore strands the old id inside existing saves, and the unguarded `item_data[<id>]` lookups (this file, lines ~163/1616/2277) raise KeyError the moment that save opens the shop or an inventory. Add the pair here and `label after_load` (GameCheck.rpy) rewrites it on load. Entries are cheap and idempotent, so keep them forever rather than tidying them away.
define ITEM_ID_RENAMES = {
    "Eat_Lunch_Rice": "Ingredient_Cook_Rice",   # 2026-08-03: given its own art, was borrowing the barbecue icon
    }

# ==================================================
define item_data = { # Item Database
# ==================================================
    # ==================================================
    # Unique
    # ==================================================
    "Unique_Key_Home" : {
        "icon"  : "images/UI/Item/Unique_Key_Home.webp",
        "name"  : "Home Key",
        "valu"  : 0,
        "cons"  : False,
        "type"  : ["unique", "key"],
        "tags"  : [],
        "info"  : "There's a key to open the front door and a key to open the garage.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    # ==================================================
    # Collectible
    # ==================================================
    "Coll_Plushy_BunnyBlack" : {
        "icon"  : "images/UI/Item/Coll_Plushy_BunnyBlack.webp",
        "name"  : "Galmon Bunny (Dark)",
        "valu"  : 500,
        "cons"  : False,
        "type"  : ["collectible", "plush"],
        "tags"  : ["bunny", "cute", "gamer", "black", "gloomy"],
        "info"  : "Cute bunny monster from Monster Girl plushy series. Girls usually love it! Give it to a [C_Per]dateable character[C_Off] so they remember you every night.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Dat]{b}Unique:{/b}[C_Off] [C_Pos]Increase up to 1% love per day[C_Off]",
        },
    "Coll_Plushy_BunnyPink" : {
        "icon"  : "images/UI/Item/Coll_Plushy_BunnyPink.webp",
        "name"  : "Galmon Bunny (Girly)",
        "valu"  : 500,
        "cons"  : False,
        "type"  : ["collectible", "plush"],
        "tags"  : ["bunny", "cute", "gamer", "pink", "girly"],
        "info"  : "Cute bunny monster from Monster Girl plushy series. Girls usually love it! Give it to a [C_Per]dateable character[C_Off] so they remember you every night.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Dat]{b}Unique:{/b}[C_Off] [C_Pos]Increase up to 1% love per day[C_Off]",
        },
    "Coll_Plushy_BunnyRed" : {
        "icon"  : "images/UI/Item/Coll_Plushy_BunnyRed.webp",
        "name"  : "Galmon Bunny (Super)",
        "valu"  : 500,
        "cons"  : False,
        "type"  : ["collectible", "plush"],
        "tags"  : ["bunny", "cute", "gamer", "red", "badass"],
        "info"  : "Cute bunny monster from Monster Girl plushy series. Girls usually love it! Give it to a [C_Per]dateable character[C_Off] so they remember you every night.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Dat]{b}Unique:{/b}[C_Off] [C_Pos]Increase up to 1% love per day[C_Off]",
        },
    "Coll_Plushy_BunnyTeal" : {
        "icon"  : "images/UI/Item/Coll_Plushy_BunnyTeal.webp",
        "name"  : "Galmon Bunny (Popstar)",
        "valu"  : 500,
        "cons"  : False,
        "type"  : ["collectible", "plush"],
        "tags"  : ["bunny", "cute", "gamer", "teal", "otaku"],
        "info"  : "Cute bunny monster from Monster Girl plushy series. Girls usually love it! Give it to a [C_Per]dateable character[C_Off] so they remember you every night.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Dat]{b}Unique:{/b}[C_Off] [C_Pos]Increase up to 1% love per day[C_Off]",
        },
    "Coll_Plushy_BunnyYellow" : {
        "icon"  : "images/UI/Item/Coll_Plushy_BunnyYellow.webp",
        "name"  : "Galmon Bunny (Vibrant)",
        "valu"  : 500,
        "cons"  : False,
        "type"  : ["collectible", "plush"],
        "tags"  : ["bunny", "cute", "gamer", "yellow", "happy"],
        "info"  : "Cute bunny monster from Monster Girl plushy series. Girls usually love it! Give it to a [C_Per]dateable character[C_Off] so they remember you every night.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Dat]{b}Unique:{/b}[C_Off] [C_Pos]Increase up to 1% love per day[C_Off]",
        },

    # ==================================================
    # Usable
    # ==================================================
    # --------------------------------------------------
    # Tool
    # --------------------------------------------------
    "Tool_Cook_Pan" : {
        "icon"  : "images/UI/Item/Tool_Cook_Pan.webp",
        "name"  : "Pan",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "tool", "cooking", "store_cablow"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Tool_Cook_PanFry" : {
        "icon"  : "images/UI/Item/Tool_Cook_PanFry.webp",
        "name"  : "Frying Pan",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "tool", "cooking", "store_cablow"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Tool_Cook_Knife" : {
        "icon"  : "images/UI/Item/Tool_Cook_Knife.webp",
        "name"  : "Cooking Knife",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "tool", "cooking", "store_cablow"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    # --------------------------------------------------
    # Ingredient
    # --------------------------------------------------
    "Ingredient_Cook_Oil" : {
        "icon"  : "images/UI/Item/Ingredient_Cook_Oil.webp",
        "name"  : "Cooking Oil",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "ingredient", "cooking", "store_cabhig"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Ingredient_Cook_Butter" : {
        "icon"  : "images/UI/Item/Ingredient_Cook_Butter.webp",
        "name"  : "Butter",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "ingredient", "cooking", "store_cabhig"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Ingredient_Cook_Salt" : {
        "icon"  : "images/UI/Item/Ingredient_Cook_Salt.webp",
        "name"  : "Salt",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["usable", "ingredient", "cooking", "store_cabhig"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    # ==================================================
    # Food
    # ==================================================
    # --------------------------------------------------
    # Recipe
    # --------------------------------------------------
    "Eat_Snack_Popcorn" : {
        "icon"  : "images/UI/Item/Eat_Snack_Popcorn.webp",
        "name"  : "Popcorn",
        "valu"  : 0,
        "cons"  : True,
        "type"  : ["consumable", "food", "store_fridge"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_Pan",
                ],
            "cook_ingn" : [
                "Eat_Veg_Corn",
                ],
            "cook_ingo" : [
                "Ingredient_Cook_Butter",
                ]
            }
        },
    "Eat_Snack_SandwichEgg" : {
        "icon"  : "images/UI/Item/Eat_Snack_SandwichEgg.webp",
        "name"  : "Egg Sandwich",
        "valu"  : 10,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "fried", "store_fridge"],
        "tags"  : ["fried"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_Knife",
                ],
            "cook_ingn" : [
                "Eat_Farm_Bread",
                "Eat_Farm_Egg",
                ],
            "cook_ingo" : [
                "Eat_Farm_Cheese",
                "Eat_Meat_Ham",
                ]
            }
        },
    "Eat_Snack_SandwichCheeseHam" : {
        "icon"  : "images/UI/Item/Eat_Snack_SandwichCheeseHam.webp",
        "name"  : "Ham Sandwich",
        "valu"  : 10,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "store_fridge"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_Knife",
                ],
            "cook_ingn" : [
                "Eat_Farm_Bread",
                "Eat_Farm_Cheese",
                "Eat_Meat_Ham",
                ]
            }
        },
    "Eat_Meal_EggFried" : {
        "icon"  : "images/UI/Item/Eat_Meal_EggFried.webp",
        "name"  : "Fried Egg",
        "valu"  : 3,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "fried", "store_fridge"],
        "tags"  : ["fried"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_PanFry",
                ],
            "cook_ingn" : [
                "Eat_Farm_Egg",
                ],
            "cook_ingo" : [
                "Ingredient_Cook_Oil",
                "Ingredient_Cook_Salt",
                ],
            "cook_steps" : [
                {"id":"crack_egg",   "blk":"counter", "pre":[],            "use":"Eat_Farm_Egg",        "req":True, "cnt":1, "mg":("precision", {"var_pla": 2,     "var_grn": 80,  "var_yel": 200, "var_org": 400})},
                {"id":"add_oil",     "blk":"stove",   "pre":[],            "use":"Ingredient_Cook_Oil", "req":False,"cnt":1, "mg":None},
                {"id":"fry_egg",     "blk":"stove",   "pre":["crack_egg"], "use":None,                  "req":True, "cnt":1, "mg":("balance",   {"var_pla": calc_phy_agi_bonus, "var_npc": 1.0, "var_axi": (40, 60)})},
                {"id":"season_salt", "blk":"stove",   "pre":["fry_egg"],   "use":"Ingredient_Cook_Salt","req":False,"cnt":1, "mg":None},
                ],
            }
        },
    # --------------------------------------------------
    # Farm
    # --------------------------------------------------
    "Eat_Farm_Bread" : {
        "icon"  : "images/UI/Item/Eat_Farm_Bread.webp",
        "name"  : "Bread",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "They say it fatten, but it's a lie. Bread does not fatten. Who eats is who fatten.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Farm_Egg" : {
        "icon"  : "images/UI/Item/Eat_Farm_Egg.webp",
        "name"  : "Egg",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "Well nutritious and rich in protein. Came from the butt of a chicken.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Farm_Cheese" : {
        "icon"  : "images/UI/Item/Eat_Farm_Cheese.webp",
        "name"  : "Cheese",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    # --------------------------------------------------
    # Meat
    # --------------------------------------------------
    "Eat_Meat_Ham" : {
        "icon"  : "images/UI/Item/Eat_Meat_Ham.webp",
        "name"  : "Ham",
        "valu"  : 1,
        "cons"  : True,
        "type"  : ["consumable", "food", "animal", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Meat_Bacon" : {
        "icon"  : "images/UI/Item/Eat_Meat_Bacon.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Bacon",
        "type"  : ["consumable", "food", "meat", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Meat_Bovine" : {
        "icon"  : "images/UI/Item/Eat_Meat_Bovine.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Bovine Meat",
        "type"  : ["consumable", "food", "meat", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Meat_Chicken" : {
        "icon"  : "images/UI/Item/Eat_Meat_Chicken.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Chicken",
        "type"  : ["consumable", "food", "meat", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Meat_Turkey" : {
        "icon"  : "images/UI/Item/Eat_Meat_Turkey.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Turkey",
        "type"  : ["consumable", "food", "meat", "store_fridge"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },

    # --------------------------------------------------
    # Sea
    # --------------------------------------------------
    "Eat_Sea_Crab" : {
        "icon"  : "images/UI/Item/Eat_Sea_Crab.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Crab",
        "type"  : ["consumable", "food", "sea"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Sea_FishSalmon" : {
        "icon"  : "images/UI/Item/Eat_Sea_FishSalmon.webp",
        "valu"  : 25,
        "cons"  : True,
        "name"  : "Salmon",
        "type"  : ["consumable", "food", "sea"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_int_bonus += 3
stat_phy_bonus += 3
stat_cha_bonus += 3
msg.msg(renpy.translate_string("[C_Pos]3% bonus[C_Off] for INT, PHY, and CHA gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases INT, PHY, and CHA gaining by 3%[C_Off]",
        },
    "Eat_Sea_Shrimp" : {
        "icon"  : "images/UI/Item/Eat_Sea_Shrimp.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Shrimp",
        "type"  : ["consumable", "food", "sea"],
        "tags"  : ["raw"],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },

    # --------------------------------------------------
    # Vegetals
    # --------------------------------------------------
    "Eat_Veg_Apple" : {
        "icon"  : "images/UI/Item/Eat_Veg_Apple.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Apple",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_int_bonus += 5
msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for INT gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases INT gaining by 5%[C_Off]",
        },
    "Eat_Veg_Banana" : {
        "icon"  : "images/UI/Item/Eat_Veg_Banana.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Banana",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_phy_bonus += 5
msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for PHY gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases PHY gaining by 5%[C_Off]",
        },
    "Eat_Veg_Carrot" : {
        "icon"  : "images/UI/Item/Eat_Veg_Carrot.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Carrot",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_cha_bonus += 5
msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for CHA gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases CHA gaining by 5%[C_Off]",
        },
    "Eat_Veg_Chilli" : {
        "icon"  : "images/UI/Item/Eat_Veg_Chilli.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Chilli",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Corn" : {
        "icon"  : "images/UI/Item/Eat_Veg_Corn.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Corn",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Cucumber" : {
        "icon"  : "images/UI/Item/Eat_Veg_Cucumber.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Cucumber",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Garlic" : {
        "icon"  : "images/UI/Item/Eat_Veg_Garlic.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Garlic",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Grape" : {
        "icon"  : "images/UI/Item/Eat_Veg_Grape.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Grape",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Lemon" : {
        "icon"  : "images/UI/Item/Eat_Veg_Lemon.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Lemon",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_cha_bonus += 5
msg.msg(renpy.translate_string("[C_Pos]5% bonus[C_Off] for CHA gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases CHA gaining by 5%[C_Off]",
        },
    "Eat_Veg_Lettuce" : {
        "icon"  : "images/UI/Item/Eat_Veg_Lettuce.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Lettuce",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Mango" : {
        "icon"  : "images/UI/Item/Eat_Veg_Mango.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Mango",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Olive" : {
        "icon"  : "images/UI/Item/Eat_Veg_Olive.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Olive",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Onion" : {
        "icon"  : "images/UI/Item/Eat_Veg_Onion.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Onion",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Orange" : {
        "icon"  : "images/UI/Item/Eat_Veg_Orange.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Orange",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
stat_cha_bonus += 3
stat_phy_bonus += 3
msg.msg(renpy.translate_string("[C_Pos]3% bonus[C_Off] for CHA and PHY gaining"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Pos]Increases CHA and PHY gaining by 3%[C_Off]",
        },
    "Eat_Veg_PassionFruit" : {
        "icon"  : "images/UI/Item/Eat_Veg_PassionFruit.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Passion Fruit",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Peach" : {
        "icon"  : "images/UI/Item/Eat_Veg_Peach.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Peach",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Peanut" : {
        "icon"  : "images/UI/Item/Eat_Veg_Peanut.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Peanut",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Pear" : {
        "icon"  : "images/UI/Item/Eat_Veg_Pear.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Pear",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Pea" : {
        "icon"  : "images/UI/Item/Eat_Veg_Pea.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Pea",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Pepper" : {
        "icon"  : "images/UI/Item/Eat_Veg_Pepper.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Pepper",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Pineapple" : {
        "icon"  : "images/UI/Item/Eat_Veg_Pineapple.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Pineapple",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Potato" : {
        "icon"  : "images/UI/Item/Eat_Veg_Potato.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Potato",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_PotatoSweet" : {
        "icon"  : "images/UI/Item/Eat_Veg_PotatoSweet.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Sweet Potato",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Strawberry" : {
        "icon"  : "images/UI/Item/Eat_Veg_Strawberry.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Strawberry",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Veg_Tomato" : {
        "icon"  : "images/UI/Item/Eat_Veg_Tomato.webp",
        "valu"  : 15,
        "cons"  : True,
        "name"  : "Tomato",
        "type"  : ["consumable", "food", "vegetable"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 15
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },

    # --------------------------------------------------
    # Lollipop
    # --------------------------------------------------
    "Eat_Sweet_CandyBox" : {
        "icon"  : "images/UI/Item/Eat_Sweet_CandyBox.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Candy Box",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Sweet_ChocolateBlack" : {
        "icon"  : "images/UI/Item/Eat_Sweet_ChocolateBlack.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Chocolate",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "[C_Unv]???[C_Off]",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]???[C_Off]",
        },
    "Eat_Sweet_ChocolateWhite" : {
        "icon"  : "images/UI/Item/Eat_Sweet_ChocolateWhite.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "White Chocolate",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "Here comes a mega pack with all kinds of candy. It's hard to not eat at least one.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Sweet_LollipopPink" : {
        "icon"  : "images/UI/Item/Eat_Sweet_LollipopPink.webp",
        "valu"  : 5,
        "cons"  : True,
        "name"  : "Lollipop (With Gum)",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "As if eating so much sugar wasn't bad enough, it also comes with gum inside. It contains such a high level of glucose that it just doesn't give you more energy because it's so small.",
        "fx_a"  : """
money += 5
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Sweet_LollipopRed" : {
        "icon"  : "images/UI/Item/Eat_Sweet_LollipopRed.webp",
        "valu"  : 5,
        "cons"  : True,
        "name"  : "Lollipop (Strawberry Taste)",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "It tastes like strawberry. But it's probably more because of the flavoring than the supposed strawberry itself. It contains such a high level of glucose that it just doesn't give you more energy because it's so small.",
        "fx_a"  : """
money += 5
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Sweet_LollipopYellow" : {
        "icon"  : "images/UI/Item/Eat_Sweet_LollipopYellow.webp",
        "valu"  : 5,
        "cons"  : True,
        "name"  : "Lollipop (Lemon Taste)",
        "type"  : ["consumable", "food", "sweet"],
        "tags"  : [],
        "info"  : "It tastes like lemon. But it's probably more because of the flavoring than the supposed lemon itself. It contains such a high level of glucose that it just doesn't give you more energy because it's so small.",
        "fx_a"  : """
money += 5
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    # --------------------------------------------------
    # Dessert
    # --------------------------------------------------
    "Eat_Dess_CakeChocolate" : {
        "icon"  : "images/UI/Item/Eat_Dess_CakeChocolate.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Chocolate Cake",
        "type"  : ["consumable", "food", "dessert"],
        "tags"  : [],
        "info"  : "The main dish of birthdays. Delicious enough to make you forget you're getting older.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Dess_Icecream" : {
        "icon"  : "images/UI/Item/Eat_Dess_Icecream.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Ice Cream",
        "type"  : ["consumable", "food", "dessert"],
        "tags"  : [],
        "info"  : "It has a white and creamy substance. Girls generally love it.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    # --------------------------------------------------
    # Snack
    # --------------------------------------------------
    "Eat_Snack_ChickenCroquettes" : {
        "icon"  : "images/UI/Item/Eat_Snack_ChickenCroquettes.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Chicken Croquettes",
        "type"  : ["consumable", "food", "snack"],
        "tags"  : [],
        "info"  : "A pack of fifty delicious chicken croquettes that cannot be missing in your party.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Snack_SandwichVegan" : {
        "icon"  : "images/UI/Item/Eat_Snack_SandwichVegan.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Vegan Sandwich",
        "type"  : ["consumable", "food", "snack"],
        "tags"  : [],
        "info"  : "A pack of ten vegan sandwiches for those who want to help nature, or perhaps avoid gaining too much weight.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    # --------------------------------------------------
    # Lunch
    # --------------------------------------------------
    "Eat_Lunch_PieFruit" : {
        "icon"  : "images/UI/Item/Eat_Lunch_PieFruit.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Fruit Pie",
        "type"  : ["consumable", "food", "lunch"],
        "tags"  : [],
        "info"  : "A healthier dessert for those who want something tasty without too many calories.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Lunch_PieShrimp" : {
        "icon"  : "images/UI/Item/Eat_Lunch_PieShrimp.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Shrimp Pie",
        "type"  : ["consumable", "food", "lunch"],
        "tags"  : [],
        "info"  : "For shrimp lovers, this is the perfect dish for you.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Eat_Lunch_Pizza" : {
        "icon"  : "images/UI/Item/Eat_Lunch_Pizza.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Pizza",
        "type"  : ["consumable", "food", "lunch"],
        "tags"  : [],
        "info"  : "A delicious pizza with cream cheese crust.",
        "fx_a"  : """
money += 40
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },

    "Eat_Lunch_Barbecue" : {
        "icon"  : "images/UI/Item/Eat_Lunch_Barbecue.webp",
        "valu"  : 40,
        "cons"  : True,
        "name"  : "Barbecue Skewer",
        "type"  : ["consumable", "food", "lunch", "animal", "store_fridge"],
        "tags"  : ["grilled"],
        "info"  : "Smoky beef skewers grilled over coal. Best shared with friends.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_Coal",
                ],
            "cook_ingn" : [
                "Eat_Meat_Bovine",
                ],
            "cook_ingo" : [
                "Eat_Meat_Ham",
                ],
            "cook_steps" : [
                {"id":"carry_coal",     "blk":"any",        "add":None,     "pre":[],                       "use":"Tool_Cook_Coal",     "req":True, "cnt":1, "mg":("thugofwar", {"var_pla":     calc_phy_str_bonus, "var_npc": 0.5, "var_tim": 50})},
                {"id":"put_coal",       "blk":"grill",      "add":"coal",   "pre":["carry_coal"],           "use":None,                 "req":True, "cnt":1, "mg":None},
                {"id":"light_grill",    "blk":"grill",      "add":"light",  "pre":["put_coal"],             "use":None,                 "req":True, "cnt":1, "mg":("precision", {"var_pla":     2, "var_grn": calc_cook_timer_green,  "var_yel": calc_cook_timer_yellow, "var_org": calc_cook_timer_orange})},
                {"id":"cut_meat",       "blk":"counter",    "add":None,     "pre":[],                       "use":"Eat_Meat_Bovine",    "req":True, "cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"cut_pepperoni",  "blk":"counter",    "add":None,     "pre":[],                       "use":"Eat_Meat_Ham",       "req":False,"cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"skewer",         "blk":"counter",    "add":None,     "pre":["cut_meat"],             "use":None,                 "req":True, "cnt":1, "mg":("precision", {"var_pla":     2, "var_grn": calc_cook_timer_green,  "var_yel": calc_cook_timer_yellow, "var_org": calc_cook_timer_orange})},
                {"id":"skewer_grill",   "blk":"grill",      "add":None,     "pre":["skewer","light_grill"], "use":None,                 "req":True, "cnt":1, "mg":("precision", {"var_pla":     2, "var_grn": calc_cook_timer_green,  "var_yel": calc_cook_timer_yellow, "var_org": calc_cook_timer_orange})},
                {"id":"flip_skewer",    "blk":"grill",      "add":None,     "pre":["skewer_grill"],         "use":None,                 "req":True, "cnt":3, "mg":("balance",   {"var_pla":     2.0, "var_npc": 2.0, "var_hol": calc_cook_hold_time})},
                ],
            },
        },

    "Ingredient_Cook_Rice" : {
        "icon"  : "images/UI/Item/Ingredient_Cook_Rice.webp",
        "valu"  : 10,
        "cons"  : True,
        "name"  : "Rice",
        "type"  : ["consumable", "food", "lunch", "vegetable", "store_fridge"],
        "tags"  : ["cooked"],
        "info"  : "fluffy rice to mix into the main dish.",
        "fx_a"  : "None",
        "fx_i"  : "[C_Unv]None[C_Off]",
        "data"  : {
            "cook_tool" : [
                "Tool_Cook_Pan",
                ],
            "cook_ingn" : [
                "Eat_Veg_Rice",
                ],
            "cook_ingo" : [
                "Eat_Veg_Carrot",
                "Eat_Veg_Tomato",
                "Eat_Veg_Potato",
                "Eat_Veg_Onion",
                ],
            "cook_steps" : [
                {"id":"light_stove",    "blk":"stove",      "add":"light",  "pre":["put_rice", "put_water"],    "use":None,             "req":True,  "cnt":1, "mg":("precision", {"var_pla":     2, "var_grn": calc_cook_timer_green,  "var_yel": calc_cook_timer_yellow, "var_org": calc_cook_timer_orange})},
                {"id":"put_rice",       "blk":"counter",    "add":None,     "pre":[],                           "use":"Eat_Veg_Rice",   "req":True,  "cnt":1, "mg": None},
                {"id":"put_water",      "blk":"sink",       "add":None,     "pre":[],                           "use":None,             "req":True,  "cnt":1, "mg":("balance",   {"var_pla": 2.0, "var_npc": 2.0, "var_hol": calc_cook_hold_time})},
                {"id":"cut_carrot",     "blk":"counter",    "add":None,     "pre":[],                           "use":"Eat_Veg_Carrot", "req":False, "cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"put_carrot",     "blk":"counter",    "add":None,     "pre":["cut_carrot"],               "use":"Eat_Veg_Carrot", "req":False, "cnt":1, "mg": None},
                {"id":"cut_tomato",     "blk":"counter",    "add":None,     "pre":[],                           "use":"Eat_Veg_Tomato", "req":False, "cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"put_tomato",     "blk":"counter",    "add":None,     "pre":["cut_tomato"],               "use":"Eat_Veg_Tomato", "req":False, "cnt":1, "mg": None},
                {"id":"cut_potato",     "blk":"counter",    "add":None,     "pre":[],                           "use":"Eat_Veg_Potato", "req":False, "cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"put_potato",     "blk":"counter",    "add":None,     "pre":["cut_potato"],               "use":"Eat_Veg_Potato", "req":False, "cnt":1, "mg": None},
                {"id":"cut_onion",      "blk":"counter",    "add":None,     "pre":[],                           "use":"Eat_Veg_Onion",  "req":False, "cnt":1, "mg":("sequence",  {"time_pass":   calc_cook_time_pass, "var_tim": 100, "count_arrow": 10})},
                {"id":"put_onion",      "blk":"counter",    "add":None,     "pre":["cut_onion"],                "use":"Eat_Veg_Onion",  "req":False, "cnt":1, "mg": None},
                ],
            },
        },

    # --------------------------------------------------
    # Drink
    # --------------------------------------------------
    "Drink_SodaGrape" : {
        "icon"  : "images/UI/Item/Drink_SodaGrape.webp",
        "valu"  : 10,
        "cons"  : True,
        "name"  : "Soda Grape",
        "type"  : ["consumable", "drink", "soda"],
        "tags"  : ["grape"],
        "info"  : "A soda of grape, or at least, it tastes like grape.",
        "fx_a"  : """
money += 10
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_SodaGuarana" : {
        "icon"  : "images/UI/Item/Drink_SodaGuarana.webp",
        "valu"  : 10,
        "cons"  : True,
        "name"  : "Soda Guarana",
        "type"  : ["consumable", "drink", "soda"],
        "tags"  : ["guarana"],
        "info"  : "A soda of guarana, or at least, it tastes like guarana.",
        "fx_a"  : """
money += 10
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_SodaOrange" : {
        "icon"  : "images/UI/Item/Drink_SodaOrange.webp",
        "valu"  : 10,
        "cons"  : True,
        "name"  : "Soda Orange",
        "type"  : ["consumable", "drink", "soda"],
        "tags"  : ["orange"],
        "info"  : "A soda of orange, or at least, it tastes like orange.",
        "fx_a"  : """
money += 10
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_SodaCola" : {
        "icon"  : "images/UI/Item/Drink_SodaCola.webp",
        "valu"  : 10,
        "cons"  : True,
        "name"  : "Soda Cola",
        "type"  : ["consumable", "drink", "soda"],
        "tags"  : ["cola"],
        "info"  : "A soda of cola, the most beloved and destructive soda.",
        "fx_a"  : """
money += 10
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_JuiceGrape" : {
        "icon"  : "images/UI/Item/Drink_JuiceGrape.webp",
        "valu"  : 20,
        "cons"  : True,
        "name"  : "Juice Grape",
        "type"  : ["consumable", "drink", "juice"],
        "tags"  : ["grape"],
        "info"  : "A juice of grape,it isn't as healthy as natural juices because of preservatives, but at least it is not soda.",
        "fx_a"  : """
money += 20
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_JuiceGuarana" : {
        "icon"  : "images/UI/Item/Drink_JuiceGuarana.webp",
        "valu"  : 20,
        "cons"  : True,
        "name"  : "Juice Guarana",
        "type"  : ["consumable", "drink", "juice"],
        "tags"  : ["guarana"],
        "info"  : "A juice of guarana, it isn't as healthy as natural juices because of preservatives, but at least it is not soda.",
        "fx_a"  : """
money += 20
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    "Drink_JuiceOrange" : {
        "icon"  : "images/UI/Item/Drink_JuiceOrange.webp",
        "valu"  : 20,
        "cons"  : True,
        "name"  : "Juice Orange",
        "type"  : ["consumable", "drink", "juice"],
        "tags"  : ["orange"],
        "info"  : "A juice of orange, it isn't as healthy as natural juices because of preservatives, but at least it is not soda.",
        "fx_a"  : """
money += 20
msg.msg(renpy.translate_string("[C_Unv]Sorry, the developer is too dumb and doesn't know what effect to put on this item. Just get your money back.[C_Off]"))
inventory.remove(a_item_3)
        """,
        "fx_i"  : "[C_Unv]None[C_Off]",
        },
    }

# ==================================================
# Mechanics
# ==================================================
# --------------------------------------------------
label item_use:
# --------------------------------------------------
    python:
        # a_item_3 is the item instance
        if a_item_3.data["cons"]:  # If consumable
            # Execute effect
            if a_item_3.data["fx_a"] != "None":
                exec(a_item_3.data["fx_a"])
            
            # Apply quality bonuses if they exist
            if a_item_3.quality is not None:
                if a_item_3.quality >= 80:
                    msg.msg(renpy.translate_string("[C_Pos]This tastes amazing![C_Off]"))
                elif a_item_3.quality <= 30:
                    msg.msg(renpy.translate_string("[C_Neg]Ugh, this is barely edible...[C_Off]"))
            
            # Remove from inventory
            inventory.remove(a_item_3)

    jump UI_show_Item_BACK

# --------------------------------------------------
label item_check: # Check Cart
# --------------------------------------------------
    python:
        if item_cart != []:
            for buceta in item_cart:
                item_cart.remove(buceta)
                inventory.append(buceta)
    return

# --------------------------------------------------
label item_storage_fridge_add: # Item From Inventory To Fridge
# --------------------------------------------------
    python:
        if a_item_3 in inventory:
            inventory_fridge.append(a_item_3)
            inventory.remove(a_item_3)

    jump UI_Inventory_Fridge_BACK

# --------------------------------------------------
label item_storage_fridge_get: # Item From Fridge To Inventory
# --------------------------------------------------
    python:
        if a_item_3 in inventory_fridge:
            inventory_fridge.remove(a_item_3)
            inventory.append(a_item_3)

    jump UI_Inventory_Fridge_BACK

# --------------------------------------------------
label item_add: # Item Add To Cart
# --------------------------------------------------
    python:        
        if money >= item_data[a_item_3]["valu"]:
            money -= item_data[a_item_3]["valu"]
            money = round(money, 2)
            AddItem_Inventory(a_item_3, 1, None, item_cart) # Create new item instance and add to cart
            item_sale.remove(a_item_3)  # Remove from sale list
        else:
            msg.msg(renpy.translate_string("More money is required."))

    jump UI_show_Item_BACK

# --------------------------------------------------
label item_rem: # Item Remove From Cart
# --------------------------------------------------
    python:
        money += a_item_3.data["valu"]
        money = round(money, 2)
        item_cart.remove(a_item_3)
        item_sale.append(a_item_3.item_id)  # Add ID back to sale

    jump UI_show_Item_BACK

# ==================================================
# Screen
# ==================================================
# --------------------------------------------------
label UI_show_Item:
# --------------------------------------------------
    call hide_ui from _call_hide_ui_129
    show screen UI_show_Item
    $ a_item_0 = 0
    $ a_item_1 = "0"
    $ a_item_2 = "0"
    $ a_item_3 = "0"
    $ ui.interact()

    label UI_show_Item_BACK:
        pass

    $ renpy.pause(hard=True)

# --------------------------------------------------
screen UI_show_Item():
# --------------------------------------------------
    #add "UI/BG0.webp"
    hbox:
        frame:
            background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
            xsize 1280 ysize 1080 xpadding 50 ypadding 50 xalign 0.0 yalign 0.0
            vbox:
                spacing 50
                vbox:
                    xalign 0.5
                    vpgrid:
                        spacing 45
                        cols 5
                        python:
                            grouped_items = {}
                            for buceta in inventory:
                                # Group by BOTH item_id AND quality
                                quality_key = buceta.quality if buceta.quality is not None else "None"
                                group_key = (buceta.item_id, quality_key)
                                
                                if group_key not in grouped_items:
                                    grouped_items[group_key] = []
                                grouped_items[group_key].append(buceta)

                        # Loop through grouped items
                        for buceta, xereca in grouped_items.items():
                            $ first_instance = xereca[0]
                            
                            frame:
                                background None
                                xsize 200
                                ysize 200
                                xpadding 0
                                ypadding 0
                                button:
                                    add first_instance.data["icon"] at Zoom_04
                                    at transform:
                                        on idle:
                                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                                        on hover:
                                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                                    action [
                                        SetVariable("a_item_1", first_instance.data["name"]),
                                        SetVariable("a_item_2", first_instance.data["info"]),
                                        SetVariable("a_item_3", first_instance)
                                    ]
                                    xalign 0.5 yalign 0.5

                                hbox:
                                    yalign 1.0

                                    python:
                                        qualities = [buceta.quality for buceta in xereca if buceta.quality is not None]
                                        if qualities:
                                            avg_quality = sum(qualities) / len(qualities)
                                            stars = int(round(avg_quality))
                                            stars = max(1, min(5, stars))
                                            empty_stars = 5 - stars
                                            quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Unv]✦[C_Off]" * empty_stars
                                        else:
                                            quality_display = ""

                                    if quality_display != "":
                                        text quality_display:
                                            xalign 0.5
                                            size 30

                                    # Item count
                                    text str(len(xereca)) xalign 1.0

        vbox:
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    xsize 540
                    if a_item_1 != "0":
                        label renpy.translate_string("{b}[a_item_1]{/b}") xalign 0.5
                    vbox:
                        xalign 0.5                            
                        # Show item image
                        if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                            image a_item_3.data["icon"] xalign 0.5
                            side ("c l"):
                                area (-25,0,1280,540)
                                viewport id "ScrollItem_Description":
                                    draggable True
                                    mousewheel True
                                    xoffset 25
                                    vbox:
                                        xalign 0.5
                                        spacing 25
                                        # Show item details
                                        if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                                            if a_item_3.quality == 5:
                                                text renpy.translate_string("{b}Quality:{/b} [C_Pos]Excellent[C_Off]")
                                            elif a_item_3.quality == 4:
                                                text renpy.translate_string("{b}Quality:{/b} [C_Dat]Good[C_Off]")
                                            elif a_item_3.quality == 3:
                                                text renpy.translate_string("{b}Quality:{/b} Common")
                                            elif a_item_3.quality == 2:
                                                text renpy.translate_string("{b}Quality:{/b} [C_Neg]Poor[C_Off]")
                                            elif a_item_3.quality == 1:
                                                text renpy.translate_string("{b}Quality:{/b} [C_Drk]Terrible[C_Off]")
                                            text renpy.translate_string("{b}About:{/b}{pr}") + str(a_item_3.data["info"])
                                            text renpy.translate_string("{b}Effect:{/b}{pr}") + str(a_item_3.data["fx_i"])
                                            #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["type"]) + "[C_Off]"
                                            #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["tags"]) + "[C_Off]"
                                vbar value YScrollValue("ScrollItem_Description")
            hbox:
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    xalign 0.0
                    yalign 0.5
                    hbox:
                        xalign 0.5
                        if a_item_3 != "0":
                            if a_item_3.data["cons"]:
                                textbutton renpy.translate_string("Consume") action (Function(msg.msg, "Available soon...")) #(Function(renpy.call, "item_use"))
                            else:
                                textbutton renpy.translate_string("Consume") action None
                        else:
                            textbutton renpy.translate_string("Consume") action None
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    xalign 0.0
                    yalign 0.5
                    textbutton renpy.translate_string("Close") xalign 0.5 action Function(renpy.jump, "show_ui")

# --------------------------------------------------
label UI_Inventory_Fridge:
# --------------------------------------------------
    scene bg_home_kitchen
    call hide_ui from _call_hide_ui_130
    show screen UI_Inventory_Fridge
    $ a_item_0 = 0
    $ a_item_1 = "0"
    $ a_item_2 = "0"
    $ a_item_3 = "0"
    $ a_item_5 = "show_ui"
    $ a_item_7 = "none"
    $ ui.interact()

    label UI_Inventory_Fridge_BACK:
        pass

    $ renpy.pause(hard=True)

screen UI_Inventory_Fridge():
    hbox:
        vbox:
            # BACKPACK/INVENTORY SECTION
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    label renpy.translate_string("Backpack")
                    vbox:
                        xalign 0.5
                        
                    side ("c l"):
                        area (0,0,1280,540)
                        vpgrid id "ScrollItem_Sale":
                            draggable True mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group inventory items by item_id and quality
                            python:
                                grouped_inv = {}
                                for item in inventory:
                                    # Only show food/drink items
                                    if "food" in item.data["type"] or "drink" in item.data["type"]:
                                        quality_key = item.quality if item.quality is not None else "None"
                                        group_key = (item.item_id, quality_key)
                                        
                                        if group_key not in grouped_inv:
                                            grouped_inv[group_key] = []
                                        grouped_inv[group_key].append(item)
                            
                            for group_key, instances in grouped_inv.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background None
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0

                                    button:
                                        add first_item.data["icon"] at Zoom_04
                                        at transform:
                                            on idle:
                                                ease 0.1 outline_transform(2, "#FFF", 3.0)
                                            on hover:
                                                ease 0.1 outline_transform(10, "#FFF", 3.0)

                                        action [
                                            SetVariable("a_item_1", first_item.data["name"]),
                                            SetVariable("a_item_2", first_item.data["info"]),
                                            SetVariable("a_item_3", first_item),
                                            SetVariable("a_item_7", "inventory")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    # Quality stars (if exists)
                                    if first_item.quality is not None:
                                        python:
                                            stars = int(first_item.quality)
                                            empty_stars = 5 - stars
                                            quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Drk]✦[C_Off]" * empty_stars
                                        
                                        text quality_display:
                                            xalign 0.5
                                            yalign 0.0
                                            size 30
                                    
                                    # Item count
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                        
                        vbar value YScrollValue("ScrollItem_Sale")
            
            # FRIDGE/STORAGE SECTION
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    hbox:
                        spacing 100
                        label renpy.translate_string("Storage")
                        
                    side ("c l"):
                        area (0,0,1280,540)
                        vpgrid id "ScrollItem_Cash":
                            draggable True mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group fridge items by item_id and quality
                            python:
                                grouped_fridge = {}
                                for item in inventory_fridge:
                                    quality_key = item.quality if item.quality is not None else "None"
                                    group_key = (item.item_id, quality_key)
                                    
                                    if group_key not in grouped_fridge:
                                        grouped_fridge[group_key] = []
                                    grouped_fridge[group_key].append(item)
                            
                            for group_key, instances in grouped_fridge.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background None
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0

                                    button:
                                        add first_item.data["icon"] at Zoom_04
                                        at transform:
                                            on idle:
                                                ease 0.1 outline_transform(2, "#FFF", 3.0)
                                            on hover:
                                                ease 0.1 outline_transform(10, "#FFF", 3.0)
                                        action [
                                            SetVariable("a_item_1", first_item.data["name"]),
                                            SetVariable("a_item_2", first_item.data["info"]),
                                            SetVariable("a_item_4", first_item.data["valu"]),
                                            SetVariable("a_item_3", first_item),
                                            SetVariable("a_item_7", "fridge")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    # Quality stars (if exists)
                                    if first_item.quality is not None:
                                        python:
                                            stars = int(first_item.quality)
                                            empty_stars = 5 - stars
                                            quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Drk]✦[C_Off]" * empty_stars
                                        
                                        text quality_display:
                                            xalign 0.5
                                            yalign 0.0
                                            size 30
                                    
                                    # Item count
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                        
                        vbar value YScrollValue("ScrollItem_Cash")

        # INFO PANEL (Right Side)
        vbox:
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    xsize 540
                    
                    if a_item_1 != "0":
                        label renpy.translate_string("{b}[a_item_1]{/b}") xalign 0.5
                    
                    vbox:
                        xalign 0.5
                        
                        # Show item image
                        if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                            image a_item_3.data["icon"] xalign 0.5
                                    
                        # Scrollable info area
                        side ("c l"):
                            area (-25,0,540,540)
                            viewport id "ScrollItem_Description":
                                draggable True
                                mousewheel True
                                xoffset 25
                                vbox:
                                    xalign 0.5
                                    spacing 25
                                    
                                    # Show item details
                                    if a_item_3 != "0" and hasattr(a_item_3, 'quality') and a_item_3.quality is not None:
                                        if a_item_3.quality == 5:
                                            text renpy.translate_string("{b}Quality:{/b} [C_Pos]Excellent[C_Off]")
                                        elif a_item_3.quality == 4:
                                            text renpy.translate_string("{b}Quality:{/b} [C_Dat]Good[C_Off]")
                                        elif a_item_3.quality == 3:
                                            text renpy.translate_string("{b}Quality:{/b} Common")
                                        elif a_item_3.quality == 2:
                                            text renpy.translate_string("{b}Quality:{/b} [C_Neg]Poor[C_Off]")
                                        elif a_item_3.quality == 1:
                                            text renpy.translate_string("{b}Quality:{/b} [C_Drk]Terrible[C_Off]")
                                    if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                                        text renpy.translate_string("{b}About:{/b}{pr}") + str(a_item_3.data["info"])
                                        text renpy.translate_string("{b}Effect:{/b}{pr}") + str(a_item_3.data["fx_i"])
                                        #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["type"]) + "[C_Off]"
                                        #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["tags"]) + "[C_Off]"
                            vbar value YScrollValue("ScrollItem_Description")
            hbox:
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    xalign 0.5
                    yalign 0.5
                    # Transfer buttons
                    if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                        hbox:
                            xalign 0.5
                            # Store button (Inventory → Fridge)
                            if a_item_7 == "inventory":
                                if "food" in a_item_3.data["type"] or "drink" in a_item_3.data["type"]:
                                    textbutton renpy.translate_string("Store") action (Function(renpy.call, "item_storage_fridge_add"))
                                else:
                                    textbutton renpy.translate_string("Store") action None
                            # Backpack button (Fridge → Inventory)
                            elif (a_item_7 == "fridge") and ("food" in a_item_3.data["type"] or "drink" in a_item_3.data["type"]):
                                textbutton renpy.translate_string("Backpack") action (Function(renpy.call, "item_storage_fridge_get"))
                            else:
                                textbutton renpy.translate_string("Backpack") action None
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    xalign 0.5
                    yalign 0.5
                    textbutton renpy.translate_string("Close") action Function(renpy.jump, a_item_5) xalign 0.5

# --------------------------------------------------
label UI_give_Item:
# --------------------------------------------------
    call hide_ui from _call_hide_ui_131
    show screen UI_give_Item
    $ a_item_0 = 0
    $ a_item_1 = "0"
    $ a_item_2 = "0"
    $ a_item_3 = "0"
    $ ui.interact()

    $ renpy.pause(hard=True)

# --------------------------------------------------
label UI_give_Item_confirm:
# --------------------------------------------------
    call hide_ui from _call_hide_ui_132
    
    python:
        # Get gift bonus (default 0 if not set)
        bonus = a_item_9 if hasattr(store, 'a_item_9') and a_item_9 is not None else 0
        
        # Give item to character and get reaction
        reaction = GiveItem_Character(a_item_8, bonus)
        
        # Calculate match level for reactions (only if accepted)
        if reaction == "Accept":
            if hasattr(store, 'gift_match_percent'):
                if store.gift_match_percent >= 75:
                    match_level = "perfect"
                elif store.gift_match_percent >= 50:
                    match_level = "great"
                elif store.gift_match_percent >= 25:
                    match_level = "good"
                else:
                    match_level = "okay"
            else:
                match_level = "good"  # Default fallback
        else:
            match_level = None  # Not needed for Reject/Already
        
        # Add time
        gametimemin += 5
    
    # Call character-specific reaction label
    $ a_item_0 = f"{a_item_8}_interact_gift_receive"
    call expression a_item_0 pass (reaction) from _call_expression

# --------------------------------------------------
screen UI_give_Item():
# --------------------------------------------------
    hbox:
        frame:
            background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
            xsize 1180 ysize 1080 xpadding 50 ypadding 50 xalign 0.0 yalign 0.0
            vbox:
                spacing 50
                vbox:
                    xalign 0.5
                    vpgrid:
                        spacing 45
                        cols 5

                        python:
                            xoxota = {}
                            for buceta in inventory:
                                if "collectible" in buceta.data["type"]:
                                    if buceta.item_id not in xoxota:
                                        xoxota[buceta.item_id] = []
                                    xoxota[buceta.item_id].append(buceta)

                        for buceta, xereca in xoxota.items():
                            $ xavasca = xereca[0]
                            frame:
                                background None
                                xsize 200
                                ysize 200
                                xpadding 0
                                ypadding 0
                                button:
                                    add xavasca.data["icon"] at Zoom_04
                                    at transform:
                                        on idle:
                                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                                        on hover:
                                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                                    action [
                                        SetVariable("a_item_1", xavasca.data["name"]),
                                        SetVariable("a_item_2", xavasca.data["type"]),
                                        SetVariable("a_item_4", xavasca.data["tags"]),
                                        SetVariable("a_item_3", xavasca)  # Store Item instance
                                    ]
                                    xalign 0.5 yalign 0.5
                                
                                text str(len(xereca)) xalign 1.0 yalign 1.0

        vbox:
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640 ysize 930 xpadding 50 ypadding 50 xalign 0.0 yalign 0.0
                vbox:
                    spacing 10
                    xsize 540
                    if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                        vbox:
                            xalign 0.5
                            label renpy.translate_string("{b}[a_item_1]{/b}")
                        
                        vbox:
                            xalign 0.5
                            image a_item_3.data["icon"]
                        
                        vbox:
                            xalign 0.5
                            side ("c l"):
                                area (-25,0,1280,540)
                                viewport id "ScrollItem_Description":
                                    draggable True
                                    mousewheel True
                                    xoffset 25
                                    vbox:
                                        xalign 0.5
                                        spacing 25
                                        text renpy.translate_string("{b}About:{/b}{pr}") + str(a_item_3.data["info"])
                                        text renpy.translate_string("{b}Effect:{/b}{pr}") + str(a_item_3.data["fx_i"])
                                        #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["type"]) + "[C_Off]"
                                        #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["tags"]) + "[C_Off]"
                                vbar value YScrollValue("ScrollItem_Description")
            hbox:
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320 ysize 150 xpadding 50 ypadding 50 xalign 0.0 yalign 0.0
                    hbox:
                        xalign 0.5
                        if a_item_3 != "0" and hasattr(a_item_3, 'data'):
                            if "unique" not in a_item_3.data["type"]:
                                textbutton renpy.translate_string("Give") action Jump("UI_give_Item_confirm")
                            else:
                                textbutton renpy.translate_string("Give") action None
                
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    xalign 0.0
                    yalign 0.5
                    textbutton renpy.translate_string("Cancel") action Function(renpy.jump, a_item_6)

# --------------------------------------------------
label UI_buy_Item:
# --------------------------------------------------
    call hide_ui from _call_hide_ui_133
    show screen UI_buy_Item
    $ a_item_0 = 0
    $ a_item_1 = "0"
    $ a_item_2 = "0"
    $ a_item_3 = "0"
    $ ui.interact()

    label UI_buy_Item_BACK:
        pass

    if renpy.get_screen("UI_buy_Item"):
        $ renpy.pause(hard=True)
    else:
        jump show_ui

    # set item list previously
    # $ item_sale = ["Eat_Icecream", "Eat_Sweet_LollipopPink", "Eat_Sweet_LollipopRed", "Eat_Sweet_LollipopYellow", "Drink_JuiceGrape", "Drink_JuiceGuarana", "Drink_JuiceOrange", "Drink_SodaGrape", "Drink_SodaGuarana", "Drink_SodaOrange",]

screen UI_buy_Item():
    hbox:
        vbox:
            # SALE SECTION (Available Items)
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    label renpy.translate_string("Sale")
                    vbox:
                        xalign 0.5
                        
                    side ("c l"):
                        area (0,0,1280,540)
                        vpgrid id "ScrollItem_Sale":
                            draggable True mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group sale items by item_id (items for sale are still just IDs)
                            python:
                                grouped_sale = {}
                                for item_id in item_sale:
                                    if item_id not in grouped_sale:
                                        grouped_sale[item_id] = 0
                                    grouped_sale[item_id] += 1
                            
                            for item_id, count in grouped_sale.items():
                                if item_id in item_data:
                                    $ item_info = item_data[item_id]
                                    
                                    frame:
                                        background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                                        xsize 200
                                        ysize 200
                                        xpadding 0
                                        ypadding 0
                                        
                                        imagebutton:
                                            idle item_info["icon"] at Zoom_04
                                            action [
                                                SetVariable("a_item_1", item_info["name"]),
                                                SetVariable("a_item_2", item_info["info"]),
                                                SetVariable("a_item_3", item_id),
                                                SetVariable("a_item_7", "sale")
                                            ]
                                            xalign 0.5 yalign 0.5
                                        
                                        text str(count) xalign 0.9 yalign 0.9
                                        text renpy.translate_string("[C_Dat]$") + str(item_info["valu"]) + "[C_Off]" xalign 0.1 yalign 0.1
                        
                        vbar value YScrollValue("ScrollItem_Sale")
            
            # CART SECTION (Items Being Purchased)
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    hbox:
                        spacing 100
                        label renpy.translate_string("Cart")
                        if money > 0:
                            label renpy.translate_string("Cash: [C_Pos]$")+str(money)+"[C_Off]"
                        else:
                            label renpy.translate_string("Cash: [C_Neg]$")+str(money)+"[C_Off]"
                        
                    side ("c l"):
                        area (0,0,1280,540)
                        vpgrid id "ScrollItem_Cash":
                            draggable True mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group cart items by item_id
                            python:
                                grouped_cart = {}
                                for item in item_cart:
                                    if item.item_id not in grouped_cart:
                                        grouped_cart[item.item_id] = []
                                    grouped_cart[item.item_id].append(item)
                            
                            for item_id, instances in grouped_cart.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0
                                    
                                    imagebutton:
                                        idle first_item.data["icon"] at Zoom_04
                                        action [
                                            SetVariable("a_item_1", first_item.data["name"]),
                                            SetVariable("a_item_2", first_item.data["info"]),
                                            SetVariable("a_item_4", first_item.data["valu"]),
                                            SetVariable("a_item_3", first_item),
                                            SetVariable("a_item_7", "cart")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                                    text renpy.translate_string("[C_Dat]$") + str(first_item.data["valu"]) + "[C_Off]" xalign 0.1 yalign 0.1
                        
                        vbar value YScrollValue("ScrollItem_Cash")

        # INFO PANEL (Right Side)
        vbox:
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.5
                vbox:
                    spacing 10
                    xsize 540
                    
                    if a_item_1 != "0":
                        label renpy.translate_string("{b}[a_item_1]{/b}") xalign 0.5
                    
                    vbox:
                        xalign 0.5
                        
                        # Show item image
                        if a_item_3 != "0":
                            # If from sale, use item_data
                            if a_item_7 == "sale" and a_item_3 in item_data:
                                image item_data[a_item_3]["icon"] xalign 0.5
                            # If from cart, use item instance
                            elif a_item_7 == "cart" and hasattr(a_item_3, 'data'):
                                image a_item_3.data["icon"] xalign 0.5
                        
                        # Add/Remove buttons
                        if a_item_3 != "0":
                            hbox:
                                spacing 25
                                xalign 0.5
                                label renpy.translate_string("Cart:")
                                
                                # Add button (Sale → Cart)
                                if a_item_7 == "sale" and a_item_3 in item_sale:
                                    textbutton renpy.translate_string("Add") action (Function(renpy.call, "item_add"))
                                else:
                                    textbutton renpy.translate_string("Add") action None
                                
                                # Remove button (Cart → Sale)
                                if a_item_7 == "cart" and hasattr(a_item_3, 'item_id'):
                                    textbutton renpy.translate_string("Remove") action (Function(renpy.call, "item_rem"))
                                else:
                                    textbutton renpy.translate_string("Remove") action None
                        
                        # Scrollable info area
                        side ("c l"):
                            area (-25,0,1280,540)
                            viewport id "ScrollItem_Description":
                                draggable True
                                mousewheel True
                                xoffset 25
                                vbox:
                                    xalign 0.5
                                    spacing 25
                                    
                                    # Show item details
                                    if a_item_3 != "0":
                                        # If from sale
                                        if a_item_7 == "sale" and a_item_3 in item_data:
                                            $ info = item_data[a_item_3]
                                            text renpy.translate_string("{b}Price:{/b} [C_Dat]$") + str(info["valu"]) + "[C_Off]"
                                            text renpy.translate_string("{b}About:{/b}{pr}") + str(info["info"])
                                            text renpy.translate_string("{b}Effect:{/b}{pr}") + str(info["fx_i"])
                                            #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(info["type"]) + "[C_Off]"
                                            #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(info["tags"]) + "[C_Off]"
                                        
                                        # If from cart
                                        elif a_item_7 == "cart" and hasattr(a_item_3, 'data'):
                                            text renpy.translate_string("{b}Price:{/b} [C_Dat]$") + str(a_item_3.data["valu"]) + "[C_Off]"
                                            text renpy.translate_string("{b}About:{/b}{pr}") + str(a_item_3.data["info"])
                                            text renpy.translate_string("{b}Effect:{/b}{pr}") + str(a_item_3.data["fx_i"])
                                            #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["type"]) + "[C_Off]"
                                            #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(a_item_3.data["tags"]) + "[C_Off]"
                            vbar value YScrollValue("ScrollItem_Description")
            
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640
                ysize 150
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.5
                textbutton renpy.translate_string("Continue") action Function(renpy.jump, a_item_5)

# ==================================================
label UI_Menu_Inventory_Transfer(invtop=inventory, invbot=inventory_fridge, topname="Inventory", botname="Storage", toptype="any", bottype="any"): # Universal Inventory Transfer Screen
# ==================================================
    call hide_ui from _call_hide_ui_134
    call screen UI_Menu_Inventory_Transfer(invtop, invbot, topname, botname, toptype, bottype)
    jump show_ui

# ==================================================
screen UI_Menu_Inventory_Transfer(invtop=inventory, invbot=inventory_fridge, topname="Inventory", botname="Storage", toptype="any", bottype="any"):
# ==================================================
    default selected_item = None
    default selected_name = ""
    default selected_info = ""
    default selected_source = ""
    
    #modal True
    
    hbox:
        #xpos 100
        # ===== INFO & ACTIONS PANEL =====
        vbox:            
            # Item info display
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 540
                ysize 930
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                
                if selected_item:
                    vbox:
                        spacing 25
                        
                        # Item icon
                        add selected_item.data["icon"] at Zoom_05 xalign 0.5
                        
                        # Item name
                        text renpy.translate_string("{b}") + selected_name + "{/b}" xalign 0.5 size 40
                        
                        # Item description with scrollbar
                        side ("c l"):
                            area (0, 0, 440, 600)
                            viewport id "scroll_description":
                                draggable True mousewheel True xoffset 10
                                vbox:
                                    spacing 25
                                    text renpy.translate_string("{b}About:{/b}{pr}") + selected_info justify True
                                    text renpy.translate_string("{b}Effect:{/b}{pr}") + selected_item.data["fx_i"]
                                    #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(selected_item.data["type"]) + "[C_Off]"
                                    #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(selected_item.data["tags"]) + "[C_Off]"
                                    if selected_item.quality is not None:
                                        text renpy.translate_string("{b}Quality:{/b}{pr}[C_Dat]") + str(selected_item.quality) + "[C_Off]/5"
                            vbar value YScrollValue("scroll_description")
                else:
                    text renpy.translate_string("Select an item to see details") xalign 0.5 yalign 0.5
            
            # Action buttons
            hbox:
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 270
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5

                        # Transfer down button
                        if selected_item and selected_source == "top":
                            textbutton renpy.translate_string("Move"):
                                action [
                                    Function(invtop.remove, selected_item),
                                    Function(invbot.append, selected_item),
                                    SetScreenVariable("selected_item", None),
                                    SetScreenVariable("selected_source", "")
                                ]
                        
                        # Transfer up button
                        elif selected_item and selected_source == "bot":
                            textbutton renpy.translate_string("Move"):
                                action [
                                    Function(invbot.remove, selected_item),
                                    Function(invtop.append, selected_item),
                                    SetScreenVariable("selected_item", None),
                                    SetScreenVariable("selected_source", "")
                                ]

                        # Transfer off
                        else:
                            textbutton renpy.translate_string("Move") action None
                
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 270
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        textbutton renpy.translate_string("Close") action Return()

        vbox:
            # ===== TOP INVENTORY SECTION =====
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    label topname
                    vbox:
                        xalign 0.5
                        
                    side ("c l"):
                        area (0, 0, 1280, 440)
                        vpgrid id "scroll_inv_top":
                            draggable True 
                            mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group inventory items by item_id and quality
                            python:
                                grouped_top = {}
                                for item in invtop:
                                    # Filter by type if specified
                                    if toptype != "any":
                                        if not any(t in item.data["type"] for t in toptype):
                                            continue
                                    
                                    quality_key = item.quality if item.quality is not None else "None"
                                    group_key = (item.item_id, quality_key)
                                    
                                    if group_key not in grouped_top:
                                        grouped_top[group_key] = []
                                    grouped_top[group_key].append(item)
                            
                            for group_key, instances in grouped_top.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background None
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0

                                    button:
                                        add first_item.data["icon"] at Zoom_04
                                        at transform:
                                            on idle:
                                                ease 0.1 outline_transform(2, "#FFF", 3.0)
                                            on hover:
                                                ease 0.1 outline_transform(10, "#FFF", 3.0)

                                        action [
                                            SetScreenVariable("selected_item", first_item),
                                            SetScreenVariable("selected_name", first_item.data["name"]),
                                            SetScreenVariable("selected_info", first_item.data["info"]),
                                            SetScreenVariable("selected_source", "top")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    # Quality stars (if exists)
                                    if first_item.quality is not None:
                                        python:
                                            stars = int(first_item.quality)
                                            empty_stars = 5 - stars
                                            quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Drk]✦[C_Off]" * empty_stars
                                        
                                        text quality_display:
                                            xalign 0.5
                                            yalign 0.0
                                            size 30
                                    
                                    # Item count
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                        
                        vbar value YScrollValue("scroll_inv_top")
            
            # ===== BOTTOM INVENTORY SECTION =====
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    label botname
                        
                    side ("c l"):
                        area (0,0,1280,440)
                        vpgrid id "scroll_inv_bot":
                            draggable True 
                            mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group inventory items by item_id and quality
                            python:
                                grouped_bot = {}
                                for item in invbot:
                                    # Filter by type if specified
                                    if bottype != "any":
                                        if not any(t in item.data["type"] for t in bottype):
                                            continue
                                    
                                    quality_key = item.quality if item.quality is not None else "None"
                                    group_key = (item.item_id, quality_key)
                                    
                                    if group_key not in grouped_bot:
                                        grouped_bot[group_key] = []
                                    grouped_bot[group_key].append(item)
                            
                            for group_key, instances in grouped_bot.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background None
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0

                                    button:
                                        add first_item.data["icon"] at Zoom_04
                                        at transform:
                                            on idle:
                                                ease 0.1 outline_transform(2, "#FFF", 3.0)
                                            on hover:
                                                ease 0.1 outline_transform(10, "#FFF", 3.0)
                                        action [
                                            SetScreenVariable("selected_item", first_item),
                                            SetScreenVariable("selected_name", first_item.data["name"]),
                                            SetScreenVariable("selected_info", first_item.data["info"]),
                                            SetScreenVariable("selected_source", "bot")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    # Quality stars (if exists)
                                    if first_item.quality is not None:
                                        python:
                                            stars = int(first_item.quality)
                                            empty_stars = 5 - stars
                                            quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Drk]✦[C_Off]" * empty_stars
                                        
                                        text quality_display:
                                            xalign 0.5
                                            yalign 0.0
                                            size 30
                                    
                                    # Item count
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                        
                        vbar value YScrollValue("scroll_inv_bot")

# ==================================================
# Universal Shopping Screen
# ==================================================
screen UI_Menu_Inventory_Shop(invtop=item_sale, invbot=item_cart, topname="Sale", botname="Cart", toptype="any", bottype="any"):
    
    # Store selected item info
    default selected_item = None
    default selected_item_id = None
    default selected_name = ""
    default selected_info = ""
    default selected_source = ""
    
    modal True
    
    hbox:
        vbox:
            # ===== TOP INVENTORY SECTION (SALE) =====
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    label topname
                    vbox:
                        xalign 0.5
                        
                    side ("c l"):
                        area (0,0,1280,440)
                        vpgrid id "scroll_shop_top":
                            draggable True 
                            mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group sale items (they are string IDs)
                            python:
                                grouped_top = {}
                                for item_id in invtop:
                                    # Filter by type if specified
                                    if toptype != "any":
                                        if item_id in item_data:
                                            if not any(t in item_data[item_id]["type"] for t in toptype):
                                                continue
                                    
                                    if item_id not in grouped_top:
                                        grouped_top[item_id] = 0
                                    grouped_top[item_id] += 1
                            
                            for item_id, count in grouped_top.items():
                                if item_id in item_data:
                                    $ item_info = item_data[item_id]
                                    
                                    frame:
                                        background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                                        xsize 200
                                        ysize 200
                                        xpadding 0
                                        ypadding 0

                                        button:
                                            add item_info["icon"] at Zoom_04
                                            at transform:
                                                on idle:
                                                    ease 0.1 outline_transform(2, "#FFF", 3.0)
                                                on hover:
                                                    ease 0.1 outline_transform(10, "#FFF", 3.0)

                                            action [
                                                SetScreenVariable("selected_item_id", item_id),
                                                SetScreenVariable("selected_item", None),
                                                SetScreenVariable("selected_name", item_info["name"]),
                                                SetScreenVariable("selected_info", item_info["info"]),
                                                SetScreenVariable("selected_source", "top")
                                            ]
                                            xalign 0.5 yalign 0.5
                                        
                                        # Item count
                                        text str(count) xalign 0.9 yalign 0.9
                                        # Price tag
                                        text renpy.translate_string("[C_Dat]$") + str(item_info["valu"]) + "[C_Off]" xalign 0.1 yalign 0.1
                        
                        vbar value YScrollValue("scroll_shop_top")
            
            # ===== BOTTOM INVENTORY SECTION (CART) =====
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 1280
                ysize 540
                xpadding 25
                ypadding 25
                xalign 0.0
                yalign 0.0
                vbox:
                    spacing 10
                    hbox:
                        spacing 100
                        label botname
                        if money > 0:
                            label renpy.translate_string("Cash: [C_Pos]$")+str(round(money,2))+"[C_Off]"
                        else:
                            label renpy.translate_string("Cash: [C_Neg]$")+str(round(money,2))+"[C_Off]"
                        
                    side ("c l"):
                        area (0,0,1280,440)
                        vpgrid id "scroll_shop_bot":
                            draggable True 
                            mousewheel True
                            xalign 0.5
                            xoffset 20
                            spacing 20
                            cols 5
                            
                            # Group cart items by item_id
                            python:
                                grouped_bot = {}
                                for item in invbot:
                                    # Filter by type if specified
                                    if bottype != "any":
                                        if not any(t in item.data["type"] for t in bottype):
                                            continue
                                    
                                    if item.item_id not in grouped_bot:
                                        grouped_bot[item.item_id] = []
                                    grouped_bot[item.item_id].append(item)
                            
                            for item_id, instances in grouped_bot.items():
                                $ first_item = instances[0]
                                
                                frame:
                                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                                    xsize 200
                                    ysize 200
                                    xpadding 0
                                    ypadding 0

                                    button:
                                        add first_item.data["icon"] at Zoom_04
                                        at transform:
                                            on idle:
                                                ease 0.1 outline_transform(2, "#FFF", 3.0)
                                            on hover:
                                                ease 0.1 outline_transform(10, "#FFF", 3.0)
                                        action [
                                            SetScreenVariable("selected_item", first_item),
                                            SetScreenVariable("selected_item_id", None),
                                            SetScreenVariable("selected_name", first_item.data["name"]),
                                            SetScreenVariable("selected_info", first_item.data["info"]),
                                            SetScreenVariable("selected_source", "bot")
                                        ]
                                        xalign 0.5 yalign 0.5
                                    
                                    # Item count
                                    text str(len(instances)) xalign 0.9 yalign 0.9
                                    # Price tag
                                    text renpy.translate_string("[C_Dat]$") + str(first_item.data["valu"]) + "[C_Off]" xalign 0.1 yalign 0.1
                        
                        vbar value YScrollValue("scroll_shop_bot")
        
        # ===== INFO & ACTIONS PANEL =====
        vbox:            
            # Item info display
            frame:
                background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.0
                
                if selected_item or selected_item_id:
                    vbox:
                        spacing 25
                        
                        # Get the correct data source
                        python:
                            if selected_source == "top" and selected_item_id:
                                display_data = item_data[selected_item_id]
                            elif selected_source == "bot" and selected_item:
                                display_data = selected_item.data
                            else:
                                display_data = None
                        
                        if display_data:
                            # Item icon
                            add display_data["icon"] at Zoom_05 xalign 0.5
                            
                            # Item name
                            text renpy.translate_string("{b}") + selected_name + "{/b}" xalign 0.5 size 40
                            
                            # Item description with scrollbar
                            side ("c l"):
                                area (-25, 0, 540, 560)
                                viewport id "scroll_description":
                                    draggable True mousewheel True xoffset 25
                                    vbox:
                                        spacing 25
                                        text renpy.translate_string("{b}Price:{/b} [C_Dat]$") + str(display_data["valu"]) + "[C_Off]"
                                        text renpy.translate_string("{b}About:{/b}{pr}") + display_data["info"] justify True
                                        text renpy.translate_string("{b}Effect:{/b}{pr}") + display_data["fx_i"]
                                        #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(display_data["type"]) + "[C_Off]"
                                        #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(display_data["tags"]) + "[C_Off]"
                                vbar value YScrollValue("scroll_description")
                else:
                    text renpy.translate_string("Select an item to see details") xalign 0.5 yalign 0.5
            
            # Action buttons
            hbox:
                # Buy/Add button
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5

                        # Add to cart (from sale)
                        if selected_item_id and selected_source == "top":
                            python:
                                item_price = item_data[selected_item_id]["valu"]
                                can_afford = money >= item_price
                            
                            if can_afford:
                                textbutton renpy.translate_string("Buy"):
                                    action [                                        
                                        SetVariable("money", money - item_price),
                                        Function(invtop.remove, selected_item_id),
                                        Function(invbot.append, Item(selected_item_id, quality=None)),
                                        SetScreenVariable("selected_item_id", None),
                                        SetScreenVariable("selected_source", "")
                                    ]
                            else:
                                textbutton renpy.translate_string("Buy") action NullAction()
                        
                        # Remove from cart
                        elif selected_item and selected_source == "bot":
                            textbutton renpy.translate_string("Remove"):
                                action [
                                    SetVariable("money", money + selected_item.data["valu"]),
                                    Function(invbot.remove, selected_item),
                                    Function(invtop.append, selected_item.item_id),
                                    SetScreenVariable("selected_item", None),
                                    SetScreenVariable("selected_source", "")
                                ]
                        
                        else:
                            textbutton "---" action NullAction()
                
                # Checkout button
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        textbutton renpy.translate_string("Checkout") action Return()

label UI_Menu_Inventory(a=inventory, b="Inventory", c="any"):
    call hide_ui from _call_hide_ui_135
    call screen UI_Menu_Inventory(a, b, c)
    jump show_ui

# --------------------------------------------------
screen UI_Menu_Inventory(inv=inventory, name="Inventory", type="any"):
# --------------------------------------------------
    # Store selected item info
    default selected_item = None
    default selected_name = ""
    default selected_info = ""
    
    #modal True
    
    hbox:
        #xpos 100
        
        # ===== INFO & ACTIONS PANEL =====
        vbox:
            # Item info display
            frame:
                xsize 640
                ysize 930
                xpadding 50
                ypadding 50
                xalign 0.0
                yalign 0.0
                
                if selected_item:
                    vbox:
                        spacing 25
                        
                        # Item icon
                        add selected_item.data["icon"] at Zoom_05 xalign 0.5
                        
                        # Item name
                        text renpy.translate_string("{b}") + selected_name + "{/b}" xalign 0.5 size 40
                        
                        # Item description with scrollbar
                        side ("c l"):
                            area (-25, 0, 540, 550)
                            viewport id "scroll_description":
                                draggable True mousewheel True xoffset 25
                                vbox:
                                    spacing 25
                                    
                                    # Quality display
                                    if selected_item.quality == 5:
                                        text renpy.translate_string("{b}Quality:{/b} [C_Pos]Excellent[C_Off]")
                                    elif selected_item.quality == 4:
                                        text renpy.translate_string("{b}Quality:{/b} [C_Dat]Good[C_Off]")
                                    elif selected_item.quality == 3:
                                        text renpy.translate_string("{b}Quality:{/b} Common")
                                    elif selected_item.quality == 2:
                                        text renpy.translate_string("{b}Quality:{/b} [C_Neg]Poor[C_Off]")
                                    elif selected_item.quality == 1:
                                        text renpy.translate_string("{b}Quality:{/b} [C_Drk]Terrible[C_Off]")
                                    
                                    text renpy.translate_string("{b}About:{/b}{pr}") + selected_info justify True
                                    text renpy.translate_string("{b}Effect:{/b}{pr}") + selected_item.data["fx_i"]
                                    #text "{b}Type:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(selected_item.data["type"]) + "[C_Off]"
                                    #text "{b}Category:{/b}{pr}[C_Dat]" + "[C_Off], [C_Dat]".join(selected_item.data["tags"]) + "[C_Off]"
                            vbar value YScrollValue("scroll_description")
                else:
                    text renpy.translate_string("Select an item to see details") xalign 0.5 yalign 0.5
            
            # Action buttons
            hbox:
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        
                        if selected_item:
                            if selected_item.data["cons"]:
                                textbutton renpy.translate_string("Consume") action Function(msg.msg, "Available soon...")  # (Function(renpy.call, "item_use"))
                            else:
                                textbutton renpy.translate_string("Consume") action NullAction()
                        else:
                            textbutton renpy.translate_string("Consume") action NullAction()
                
                frame:
                    background Frame(If(preferences.windowtheme == "City", "gui/frame_dark.png", "gui/frame_light.png"), gui.frame_borders, tile=gui.frame_tile)
                    xsize 320
                    ysize 150
                    xpadding 50
                    ypadding 50
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        textbutton renpy.translate_string("Close") action Return()
                        
        # ===== INVENTORY SECTION =====
        frame:
            xsize 1180
            ysize 1080
            xpadding 50
            ypadding 50
            xalign 0.0
            yalign 0.0
            vbox:
                spacing 10
                label name
                
                side ("c l"):
                    area (0, 0, 1180, 940)
                    vpgrid id "scroll_inventory":
                        draggable True
                        mousewheel True
                        xalign 0.5
                        xoffset 20
                        spacing 10
                        cols 5
                        
                        # Group inventory items by item_id and quality
                        python:
                            grouped_items = {}
                            for item in inv:
                                # Filter by type if specified
                                if type != "any":
                                    if not any(t in item.data["type"] for t in type):
                                        continue
                                
                                quality_key = item.quality if item.quality is not None else "None"
                                group_key = (item.item_id, quality_key)
                                
                                if group_key not in grouped_items:
                                    grouped_items[group_key] = []
                                grouped_items[group_key].append(item)
                        
                        for group_key, instances in grouped_items.items():
                            $ first_item = instances[0]
                            
                            frame:
                                background "#00000032"
                                xsize 200
                                ysize 200
                                xpadding 0
                                ypadding 0
                                
                                button:
                                    add first_item.data["icon"] at Zoom_04
                                    at transform:
                                        on idle:
                                            ease 0.1 outline_transform(2, "#FFF", 3.0)
                                        on hover:
                                            ease 0.1 outline_transform(10, "#FFF", 3.0)
                                    action [
                                        SetScreenVariable("selected_item", first_item),
                                        SetScreenVariable("selected_name", first_item.data["name"]),
                                        SetScreenVariable("selected_info", first_item.data["info"])
                                    ]
                                    xalign 0.5 yalign 0.5
                                
                                # Quality stars (if exists)
                                if first_item.quality is not None:
                                    python:
                                        stars = int(first_item.quality)
                                        empty_stars = 5 - stars
                                        quality_display = "[C_Dat]✦[C_Off]" * stars + "[C_Drk]✦[C_Off]" * empty_stars
                                    
                                    text quality_display:
                                        xalign 0.5
                                        yalign 0.0
                                        size 30
                                
                                # Item count
                                text str(len(instances)) xalign 0.9 yalign 0.9
                    
                    vbar value YScrollValue("scroll_inventory")
