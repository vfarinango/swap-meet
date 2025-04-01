class Vendor:
    def __init__(self,inventory=None):  #check the slides
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)

            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False



    # -----------------------------------------
    # ------------ Wave 4 ---------------------
    # -----------------------------------------

    def swap_first_item(self, other_vendor):
        #Version 1
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            instance_first_item = self.inventory[0]
            friend_first_item = other_vendor.inventory[0]

            self.inventory.remove(instance_first_item)
            other_vendor.inventory.append(instance_first_item)

            other_vendor.inventory.remove(friend_first_item)
            self.inventory.append(friend_first_item)

            return True
        
        #Q: Is order matters? Or we can just append whatever is swaped to the end of each vender's inventory list?
        #version 2 - DRYing up! (Let's discuss)

    # -----------------------------------------
    # ------------ Wave 6 ---------------------
    # -----------------------------------------

    def get_by_category(self, category):
        """
        Gets a list of items in a certain category.

        Args:
            category: a string that represents a category of item

        Returns:
            It returns a list of objects in the inventory with that category
            If there are no items in the `inventory` that match the category argument, the method returns an empty list
        """
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category
    
    def get_best_by_category(self,category):
        """
        Gets the item with the highest condition in a certain category.
        This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`

        Args:
            category: a string that represents a category of item

        Returns:
            It returns this item. The method only returns a single item even if there are duplicates items that have same category and same condition
            If there are no items in the `inventory` that match the category, it returns `None`
        """

        category_items = self.get_by_category(category)
        if not category_items:
            return None
        
        highest_condition_item = category_items[0]
        for item in category_items:
            if item.condition > highest_condition_item.condition:
                highest_condition_item = item
        return highest_condition_item

        

    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        """
        Swaps the best item of certain categories with another `Vendor`
        The best item in my inventory that matches `their_priority` category is swapped with the best item in `other_vendor`'s inventory that matches `my_priority`

        Args:
            other_vendor: represents another `Vendor` instance to trade with
            my_priority: represents a category that the `Vendor` wants to receive
            their_priority: represents a category that `other_vendor` wants to receive

        Returns:
            It returns True.
            If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
            If `other_vendor` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
        """
        if not self.inventory or not other_vendor.inventory:
            return False
        
        other_vender_wants = None
        vender_wants = None

        for item in self.inventory:
            if item.get_category() == their_priority:
                #It's important to put the other_vender_wants == None check first
                #Because "or" operation could potentially end earlier when the first condition is met
                if other_vender_wants == None or item.condition > other_vender_wants.condition:
                    other_vender_wants = item

        for item in other_vendor.inventory:
            if item.get_category() == my_priority:
                if vender_wants == None or item.condition > vender_wants.condition:
                    vender_wants = item
        #Version 1
        if not other_vender_wants or not vender_wants:
            return False
        self.inventory.remove(other_vender_wants)
        other_vendor.inventory.append(other_vender_wants)
        other_vendor.inventory.remove(vender_wants)
        self.inventory.append(vender_wants)
        return True

        #Version 2 - DRYing up! (Let's discuss)
