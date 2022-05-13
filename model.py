from dataclasses import dataclass
from typing import List


@dataclass
class OrderLine:
  sku: str
  qty: int


@dataclass
class Order:
  reference_id: int
  lines: List[OrderLine]


@dataclass
class Batch:
  reference_id: int
  sku: str
  qty: int

  def allocate(self, order_line):
    if self.sku == order_line.sku and self.qty >= order_line.qty:
      self.qty -= order_line.qty
      return True
    else:
      return False

    

