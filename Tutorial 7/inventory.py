import json
import os
from typing import List, Optional
from product import Product
from product_types import DigitalProduct, PhysicalProduct

# Resolve absolute path relative to inventory.py location
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_JSON_PATH = os.path.join(CURRENT_DIR, "inventory.json")


class Inventory:

  def __init__(self, filepath: str = DEFAULT_JSON_PATH):
    self.filepath = filepath
    self.products: List[Product] = []
    self.load_data()

  def add_product(self, product: Product) -> None:
    self.products.append(product)

  def search_product(self, product_id: str) -> Optional[Product]:
    for p in self.products:
      if p.product_id == product_id:
        return p
    return None

  def display_all(self) -> None:
    if not self.products:
      print("No products in inventory.")
      return
    for p in self.products:
      p.display_information()
      print(f"  Fulfilment: {p.get_fulfilment_info()}")
      if isinstance(p, PhysicalProduct):
        print(f"  Shipping Cost: ${p.calculate_shipping_cost():.2f}")
      print("-" * 40)

  def save_data(self) -> None:
    data = [p.to_dict() for p in self.products]
    with open(self.filepath, "w") as f:
      json.dump(data, f, indent=4)

  def load_data(self) -> None:
    try:
      with open(self.filepath, "r") as f:
        data = json.load(f)
        self.products = []
        for item in data:
          p_type = item.get("type")
          if p_type == "physical":
            p = PhysicalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"],
            )
          elif p_type == "digital":
            p = DigitalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"],
            )
          else:
            continue
          self.products.append(p)
    except (FileNotFoundError, json.JSONDecodeError):
      self.products = []