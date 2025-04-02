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
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category
    

    def get_best_by_category(self,category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        
        highest_condition_item = category_items[0]
        for item in category_items:
            if item.condition > highest_condition_item.condition:
                highest_condition_item = item
        return highest_condition_item

        
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        other_vendor_wants = self.get_best_by_category(their_priority)
        vendor_wants = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, other_vendor_wants, vendor_wants)
    


    #Optional Enhancement
    def get_newest(self):
        if not self.inventory:
            return None

        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item
    
    
    def swap_by_newest(self, other_vendor):
        #our assumption: if multiple items having same age, return the first item in inventory list
        newest_item = self.get_newest()
        other_vendor_newest_item = other_vendor.get_newest()
        return self.swap_items(other_vendor,newest_item,other_vendor_newest_item)