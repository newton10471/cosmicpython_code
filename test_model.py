from datetime import date, timedelta
import pytest

from model import Batch, OrderLine

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    sku = '12345'
    batch_qty = 10
    order_line_qty = 9
    batch = Batch(reference_id=1, sku=sku, qty=batch_qty)
    order_line = OrderLine(sku=sku, qty=order_line_qty)
    batch.allocate_order_line(order_line)
    assert(batch.qty == batch_qty - order_line_qty)

def test_can_allocate_if_available_greater_than_required():
    pytest.fail("todo")


def test_cannot_allocate_if_available_smaller_than_required():
    pytest.fail("todo")


def test_can_allocate_if_available_equal_to_required():
    pytest.fail("todo")


def test_prefers_warehouse_batches_to_shipments():
    pytest.fail("todo")


def test_prefers_earlier_batches():
    pytest.fail("todo")
