import unittest
from lab.lab6.src.saga import Orchestrator, SagaState


class SagaTests(unittest.TestCase):
    def test_successful_run(self):
        orch = Orchestrator(
            do_reserve=lambda: True,
            do_charge=lambda: True,
            do_ship=lambda: True,
        )
        state = orch.run()
        self.assertEqual(state, SagaState.DONE)

    def test_payment_failure_compensation(self):
        orch = Orchestrator(
            do_reserve=lambda: True,
            do_charge=lambda: False,  # payment fails
            do_ship=lambda: True,
        )
        state = orch.run()
        self.assertEqual(state, SagaState.FAILED)

    def test_shipment_failure_compensation(self):
        orch = Orchestrator(
            do_reserve=lambda: True,
            do_charge=lambda: True,
            do_ship=lambda: False,  # shipment fails
        )
        state = orch.run()
        self.assertEqual(state, SagaState.FAILED)

    def test_reserve_failure(self):
        orch = Orchestrator(
            do_reserve=lambda: False,  # reserve fails
            do_charge=lambda: True,
            do_ship=lambda: True,
        )
        state = orch.run()
        self.assertEqual(state, SagaState.FAILED)

    def test_invalid_transition_does_not_change_state(self):
        orch = Orchestrator()
        self.assertEqual(orch.sm.state, SagaState.INIT)
        ok = orch.sm.send("ok")  # invalid from INIT
        self.assertFalse(ok)
        self.assertEqual(orch.sm.state, SagaState.INIT)

    def test_compensation_failure_stays_in_compensating(self):
        orch = Orchestrator(
            do_reserve=lambda: True,
            do_charge=lambda: False,  # fails -> compensate
            do_ship=lambda: True,
            do_compensate=lambda: False,  # compensation fails
        )
        state = orch.run()
        self.assertEqual(state, SagaState.COMPENSATING)

    def test_action_order_success(self):
        order = []

        def reserve():
            order.append("reserve")
            return True

        def charge():
            order.append("charge")
            return True

        def ship():
            order.append("ship")
            return True

        orch = Orchestrator(do_reserve=reserve, do_charge=charge, do_ship=ship)
        state = orch.run()
        self.assertEqual(state, SagaState.DONE)
        self.assertEqual(order, ["reserve", "charge", "ship"])

    def test_action_order_payment_fail_then_compensate(self):
        order = []

        def reserve():
            order.append("reserve")
            return True

        def charge():
            order.append("charge")
            return False  # triggers compensation

        def compensate():
            order.append("compensate")
            return True

        orch = Orchestrator(do_reserve=reserve, do_charge=charge, do_ship=lambda: True, do_compensate=compensate)
        state = orch.run()
        self.assertEqual(state, SagaState.FAILED)
        self.assertEqual(order, ["reserve", "charge", "compensate"])

    def test_action_order_shipment_fail_then_compensate(self):
        order = []

        def reserve():
            order.append("reserve")
            return True

        def charge():
            order.append("charge")
            return True

        def ship():
            order.append("ship")
            return False  # triggers compensation

        def compensate():
            order.append("compensate")
            return True

        orch = Orchestrator(do_reserve=reserve, do_charge=charge, do_ship=ship, do_compensate=compensate)
        state = orch.run()
        self.assertEqual(state, SagaState.FAILED)
        self.assertEqual(order, ["reserve", "charge", "ship", "compensate"])


if __name__ == "__main__":
    unittest.main()
