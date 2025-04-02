import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

#@pytest.mark.skip
def test_items_have_default_uuid_length_id():
    item = Item()
    assert isinstance(item.id, int)
    assert len(str(item.id)) >= 32

#@pytest.mark.skip
def test_item_instances_have_different_default_ids():
    item_a = Item()
    item_b = Item()
    assert item_a.id != item_b.id

#@pytest.mark.skip
def test_items_use_custom_id_if_passed():
    item = Item(id=12345)
    assert isinstance(item.id, int)
    assert item.id == 12345

#@pytest.mark.skip
def test_item_obj_returns_text_item_for_category():
    item = Item()
    assert item.get_category() == "Item"

#@pytest.mark.skip
def test_get_item_by_id():
    test_id = 12345
    item_custom_id = Item(id=test_id)
    vendor = Vendor(
        inventory=[Item(), Item(), item_custom_id]
    )

    result_item = vendor.get_by_id(test_id)
    assert result_item is item_custom_id

#@pytest.mark.skip
def test_get_item_by_id_no_matching():
    test_id = 12345
    item_a = Item()
    item_b = Item()
    item_c = Item()

    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result_item = vendor.get_by_id(test_id)
    assert result_item is None

    items = vendor.inventory
    assert len(items) == 3
    assert item_a in items
    assert item_b in items
    assert item_c in items


#additional tests
def test_items_have_default_age():
    item = Item()
    assert item.age == 0

def test_items_have_custom_age():
    item = Item(age=5)
    assert item.age == 5


# Additional test for Item id attribute exception handling
def test_id_exception():
    with pytest.raises(TypeError):
        Item(id ="aaa")

# Additional test for Item condition Description
def test_condition_description_matches():
    # Arrange
    item_a = Item()
    item_b = Item(condition = 5)
    item_c = Item(condition = 4)
    item_d = Item(condition = 3)
    item_e = Item(condition = 2)
    item_f = Item(condition = 1)

    # Act
    item_a_condition = item_a.condition_description()
    item_b_condition = item_b.condition_description()
    item_c_condition = item_c.condition_description()
    item_d_condition = item_d.condition_description()
    item_e_condition = item_e.condition_description()
    item_f_condition = item_f.condition_description()

    # Assert
    assert item_a_condition == 'Heavily Used'
    assert item_b_condition == "New"
    assert item_c_condition == "Like new"
    assert item_d_condition == "Very Good"
    assert item_e_condition == "Good"
    assert item_f_condition == "Acceptable"
