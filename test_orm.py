from sqlalchemy.orm import Session as session
import model
import pytest

def test_orderline_mapper_can_load_lines(session):
  session.execute(
    'INSERT INTO order_lines (order, sku, qty) VALUES '
    '("order1", "RED-CHAIR", 12),'
    '("order1", "RED-TABLE", 13),'
    '("order2", "BLUE-LIPSTICK", 14)'
  )
  expected = [
    model.OrderLine("order1", "RED-CHAIR", 12),
    model.OrderLine("order1", "RED-TABLE", 13),
    model.OrderLine("order1", "BLUE-LIPSTICK", 14)
  ]
  assert session.query(model.OrderLine).all() == expected