import logging
from .state_machine import StateMachine, SagaState
from typing import Callable


# Default side-effect actions (can be injected/mocked in tests)
def reserve_stock() -> bool:
    return True


def charge_payment() -> bool:
    return True


def create_shipment() -> bool:
    return True


def compensate() -> bool:
    # Compensation always attempts and returns True for demo purposes
    return True


class Orchestrator:
    def __init__(self,
                 do_reserve: Callable[[], bool] = reserve_stock,
                 do_charge: Callable[[], bool] = charge_payment,
                 do_ship: Callable[[], bool] = create_shipment,
                 do_compensate: Callable[[], bool] = compensate):
        self.sm = StateMachine(SagaState.INIT)
        self.do_reserve = do_reserve
        self.do_charge = do_charge
        self.do_ship = do_ship
        self.do_compensate = do_compensate
        self._log = logging.getLogger("lab6.saga")
        self._wire()

    def _wire(self):
        self.sm.add_transition(SagaState.INIT, "start", SagaState.RESERVE_STOCK, lambda: True)
        self.sm.add_transition(SagaState.RESERVE_STOCK, "ok", SagaState.CHARGE_PAYMENT, self.do_reserve)
        self.sm.add_transition(SagaState.CHARGE_PAYMENT, "ok", SagaState.CREATE_SHIPMENT, self.do_charge)
        self.sm.add_transition(SagaState.CREATE_SHIPMENT, "ok", SagaState.DONE, self.do_ship)

        # Echecs
        self.sm.add_transition(SagaState.RESERVE_STOCK, "ko", SagaState.FAILED, lambda: True)
        self.sm.add_transition(SagaState.CHARGE_PAYMENT, "ko", SagaState.COMPENSATING, lambda: True)
        self.sm.add_transition(SagaState.CREATE_SHIPMENT, "ko", SagaState.COMPENSATING, lambda: True)

        # Compensation
        self.sm.add_transition(SagaState.COMPENSATING, "compensate", SagaState.FAILED, self.do_compensate)

    def run(self) -> SagaState:
        # start
        self._log.debug("orchestrator run start")
        self.sm.send("start")
        if not self.sm.send("ok"):
            # reserve failed => FAIL directly
            self.sm.send("ko")
            state = self.sm.state
            self._log.debug("orchestrator end: %s", state.name)
            return state
        if not self.sm.send("ok"):
            # payment failed => COMPENSATING then compensate
            self.sm.send("ko")
            self.sm.send("compensate")
            state = self.sm.state
            self._log.debug("orchestrator end: %s", state.name)
            return state
        if not self.sm.send("ok"):
            # shipment failed => COMPENSATING then compensate
            self.sm.send("ko")
            self.sm.send("compensate")
            state = self.sm.state
            self._log.debug("orchestrator end: %s", state.name)
            return state
        state = self.sm.state
        self._log.debug("orchestrator end: %s", state.name)
        return state
