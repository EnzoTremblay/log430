import pytest
from saga.orchestrator import OrderSaga


def test_successful_flow():
    s = OrderSaga()
    s.reserve_stock_ok = True
    s.charge_payment_ok = True
    s.create_shipment_ok = True
    final_state = s.run()
    assert final_state == 'COMPLETE'


def test_payment_failure_compensation():
    s = OrderSaga()
    s.reserve_stock_ok = True
    s.charge_payment_ok = False
    final_state = s.run()
    assert final_state == 'FAILED'


def test_shipment_failure_compensation():
    s = OrderSaga()
    s.reserve_stock_ok = True
    s.charge_payment_ok = True
    s.create_shipment_ok = False
    final_state = s.run()
    assert final_state == 'FAILED'
