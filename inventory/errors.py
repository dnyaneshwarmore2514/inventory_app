class InventoryError(Exception):
    """Base class for all inventory errors."""


class OutOfStockError(InventoryError):
    """Raised when you try to remove more items than exist."""