import logging
from enum import Enum, auto
from typing import Callable, Dict, Tuple


class SagaState(Enum):
    INIT = auto()
    RESERVE_STOCK = auto()
    CHARGE_PAYMENT = auto()
    CREATE_SHIPMENT = auto()
    DONE = auto()
    COMPENSATING = auto()
    FAILED = auto()


TransitionKey = Tuple[SagaState, str]
Action = Callable[[], bool]


class StateMachine:
    def __init__(self, initial: SagaState):
        self.state = initial
        self.transitions: Dict[TransitionKey, Tuple[SagaState, Action]] = {}
        self._log = logging.getLogger("lab6.saga")

    def add_transition(self, src: SagaState, event: str, dst: SagaState, action: Action):
        self.transitions[(src, event)] = (dst, action)
        self._log.debug("transition added: %s --%s--> %s", src.name, event, dst.name)

    def send(self, event: str) -> bool:
        key = (self.state, event)
        self._log.debug("event: %s (state=%s)", event, self.state.name)
        if key not in self.transitions:
            self._log.warning("no transition for event '%s' in state %s", event, self.state.name)
            return False
        dst, action = self.transitions[key]
        ok = True
        if action:
            try:
                ok = bool(action())
            except Exception as exc:  # pragma: no cover - safety
                self._log.exception("action raised exception: %s", exc)
                ok = False
        if ok:
            old = self.state
            self.state = dst
            self._log.debug("transition: %s --%s--> %s", old.name, event, self.state.name)
        else:
            self._log.debug("action returned false; staying in %s", self.state.name)
        return ok
