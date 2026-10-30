from abc import ABC, abstractmethod


class Product(ABC):

  def __init__(self, product_id: str, name: str, price: float, stock: int):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.stock = stock

  def update_stock(self, quantity: int) -> None:
    self.stock += quantity

  def display_information(self) -> None:
    print(
        f"ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f}"
        f" | Stock: {self.stock}"
    )

  @abstractmethod
  def get_fulfilment_info(self) -> str:
    """Returns fulfilment instructions specific to the product type."""
    pass

  def to_dict(self) -> dict:
    """Helper method for JSON serialization."""
    return {
        "product_id": self.product_id,
        "name": self.name,
        "price": self.price,
        "stock": self.stock,
    }