class AHTStrategy:

    def calculate(self, handle_time, inbound_tx):
        if inbound_tx == 0:
            return 0
        return handle_time / inbound_tx


class ACWStrategy:

    def calculate(self, acw, inbound_tx):
        if inbound_tx == 0:
            return 0
        return acw / inbound_tx