class Vendor:
    def __init__(self,inventory=None): 
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
            self.remove(my_item)
            other_vendor.add(my_item)

            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False



    # -----------------------------------------
    # ------------ Wave 4 ---------------------
    # -----------------------------------------

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    


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
        other_vendor_wants = self.get_best_by_category(their_priority)
        vendor_wants = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, other_vendor_wants, vendor_wants)
    


    #Optional Enhancement
    def get_newest(self):
        if not self.inventory:
            return False

        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item
    
    
    def swap_by_newest(self, other_vendor):
        newest_item = self.get_newest()
        other_vendor_newest_item = other_vendor.get_newest()
        return self.swap_items(other_vendor,newest_item,other_vendor_newest_item)