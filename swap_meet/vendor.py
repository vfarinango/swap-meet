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
        #other_vendor = the friend the vendor is swapping with
        # my_item = the item that this vendor will give friend
        #their_item = the item that friend vendor will give this vendor

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
        # Consider the first item in the instance's inventory (self)
        # and consider the first item in the friend's inventory (other_vendor)

        # Remove the first item from instance's inventory and 
        # add the friend's first item

        # Remove the first item from the friend's inventory and 
        # add instance's first item

        #return True
        #Else return False

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
        #Your inputs:

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
        #Your inputs: