from .errors import OutOfStockError


class Inventory:
    """Keeps track of how many of each item we have."""

    def __init__(self) -> None:
        self._items: dict[str, int] = {}

    def add(self, name: str, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("qty must be positive")
        self._items[name] = self._items.get(name, 0) + qty

    def remove(self, name: str, qty: int = 1) -> None:
        have = self._items.get(name, 0)
        if qty > have:
            raise OutOfStockError(f"only {have} of {name!r} left, wanted {qty}")
        self._items[name] = have - qty

    def count(self, name: str) -> int:
        return self._items.get(name, 0)