import pytest

from inventory import Inventory, OutOfStockError


def test_add_and_count():
    inv = Inventory()
    inv.add("pen", 5)
    inv.add("pen", 2)
    assert inv.count("pen") == 7


def test_remove_reduces_count():
    inv = Inventory()
    inv.add("book", 3)
    inv.remove("book", 2)
    assert inv.count("book") == 1


def test_remove_too_many_raises():
    inv = Inventory()
    inv.add("cup", 1)
    with pytest.raises(OutOfStockError):
        inv.remove("cup", 5)