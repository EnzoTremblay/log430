from transitions import Machine

class OrderSaga:
    states = [
        'INIT', 'RESERVE_STOCK', 'CHARGE_PAYMENT', 'CREATE_SHIPMENT',
        'COMPLETE', 'COMPENSATE_STOCK', 'REFUND_PAYMENT', 'FAILED'
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=OrderSaga.states, initial='INIT')
        self._define_transitions()
        # Simulated external outcomes (can be set in tests)
        self.reserve_stock_ok = True
        self.charge_payment_ok = True
        self.create_shipment_ok = True

    def _define_transitions(self):
        self.machine.add_transition('start', 'INIT', 'RESERVE_STOCK', after='reserve_stock')
        self.machine.add_transition('next', 'RESERVE_STOCK', 'CHARGE_PAYMENT', conditions='is_reserve_stock_ok', after='charge_payment')
        self.machine.add_transition('next', 'CHARGE_PAYMENT', 'CREATE_SHIPMENT', conditions='is_charge_payment_ok', after='create_shipment')
        self.machine.add_transition('next', 'CREATE_SHIPMENT', 'COMPLETE', conditions='is_create_shipment_ok')

        # Failure paths
        self.machine.add_transition('fail', 'RESERVE_STOCK', 'FAILED', unless='is_reserve_stock_ok')
        self.machine.add_transition('fail', 'CHARGE_PAYMENT', 'COMPENSATE_STOCK', unless='is_charge_payment_ok', after='compensate_stock')
        self.machine.add_transition('fail', 'CREATE_SHIPMENT', 'REFUND_PAYMENT', unless='is_create_shipment_ok', after='refund_payment')
        self.machine.add_transition('finalize_fail', 'REFUND_PAYMENT', 'COMPENSATE_STOCK', after='compensate_stock')
        self.machine.add_transition('finalize', 'COMPENSATE_STOCK', 'FAILED')

    # Guards
    def is_reserve_stock_ok(self):
        return self.reserve_stock_ok

    def is_charge_payment_ok(self):
        return self.charge_payment_ok

    def is_create_shipment_ok(self):
        return self.create_shipment_ok

    # Actions
    def reserve_stock(self):
        pass

    def charge_payment(self):
        pass

    def create_shipment(self):
        pass

    def compensate_stock(self):
        pass

    def refund_payment(self):
        pass

    # Orchestrate
    def run(self):
        self.start()
        if self.state == 'RESERVE_STOCK':
            if self.is_reserve_stock_ok():
                self.next()
            else:
                self.fail()
        if self.state == 'CHARGE_PAYMENT':
            if self.is_charge_payment_ok():
                self.next()
            else:
                self.fail()
        if self.state == 'CREATE_SHIPMENT':
            if self.is_create_shipment_ok():
                self.next()
            else:
                self.fail()
        if self.state in ['REFUND_PAYMENT']:
            self.finalize_fail()
        if self.state in ['COMPENSATE_STOCK']:
            self.finalize()
        return self.state
