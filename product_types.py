from product import Product
from shippable import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):

  def __init__(
      self, product_id: str, name: str, price: float, stock: int, weight: float
  ):
    super().__init__(product_id, name, price, stock)
    self.weight = weight  # In kg

  def display_information(self) -> None:
    super().display_information()
    print(f"  -> Type: Physical | Weight: {self.weight} kg")

  def get_fulfilment_info(self) -> str:
    return f"Requires physical packaging and shipping (Weight: {self.weight} kg)."

  def calculate_shipping_cost(self) -> float:
    # Example rule: $5.00 base fee + $2.50 per kg
    return 5.00 + (self.weight * 2.50)

  def to_dict(self) -> dict:
    data = super().to_dict()
    data.update({"type": "physical", "weight": self.weight})
    return data


class DigitalProduct(Product):

  def __init__(
      self,
      product_id: str,
      name: str,
      price: float,
      stock: int,
      download_size: float,
  ):
    super().__init__(product_id, name, price, stock)
    self.download_size = download_size  # In MB

  def display_information(self) -> None:
    super().display_information()
    print(f"  -> Type: Digital | Download Size: {self.download_size} MB")

  def get_fulfilment_info(self) -> str:
    return f"Delivered digitally via email/download link ({self.download_size} MB)."

  def to_dict(self) -> dict:
    data = super().to_dict()
    data.update({"type": "digital", "download_size": self.download_size})
    return data