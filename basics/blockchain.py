import hashlib
import sawtooth_sdk.processor as processor


# Define the transaction family name
FAMILY_NAME = "simple_blockchain"


class SimpleBlockchainTransactionHandler(handler.TransactionHandler):
    def __init__(self):
        self._family_name = FAMILY_NAME

    def family_name(self):
        return self._family_name

    def family_versions(self):
        return ["1.0"]

    def apply(self, transaction, context):
        header = transaction.header
        payload = transaction.payload.decode("utf-8")
        address = self.make_address(payload)

        state = context.get_state([address])

        if state:
            state_str = state[0].data.decode("utf-8")
            state_value = int(state_str)
        else:
            state_value = 0

        updated_value = state_value + 1

        context.set_state({address: str(updated_value).encode("utf-8")})

    def make_address(self, payload):
        payload_hash = hashlib.sha512(payload.encode("utf-8")).hexdigest()
        return FAMILY_NAME.encode("utf-8") + payload_hash[:64].encode("utf-8")


if __name__ == "__main__":
    processor = handler.TransactionProcessor(url="tcp://localhost:4004")
    handler = SimpleBlockchainTransactionHandler()
    processor.add_handler(handler)
    print("Starting transaction processor...")
    try:
        processor.start()
    except KeyboardInterrupt:
        processor.stop()
