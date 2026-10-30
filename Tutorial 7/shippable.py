from abc import ABC, abstractmethod


class CanBeShipped(ABC):

  @abstractmethod
  def calculate_shipping_cost(self) -> float:
    """Calculates shipping cost for the item."""
    pass