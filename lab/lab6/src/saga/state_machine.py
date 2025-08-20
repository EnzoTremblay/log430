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

    def add_transition(self, src: SagaState, event: str, dst: SagaState, action: Action):
        self.transitions[(src, event)] = (dst, action)

    def send(self, event: str) -> bool:
        key = (self.state, event)
        if key not in self.transitions:
            return False
        dst, action = self.transitions[key]
        ok = True
        if action:
            ok = bool(action())
        self.state = dst if ok else self.state
        return ok
