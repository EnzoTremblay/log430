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


if __name__ == "__main__":
    unittest.main()
