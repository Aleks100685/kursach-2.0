class Transaction:
    def __init__(self, data):
        self.id = data.get("id", None)
        self.state = data.get("state", None)
        self.date = data.get("date", None)
        self.amount = float(data["operationAmount"]["amount"]) if "operationAmount" in data and "amount" in data["operationAmount"] else None
        self.currency = data["operationAmount"]["currency"]["name"] if "operationAmount" in data and "currency" in data["operationAmount"] else None
        self.description = data.get("description", None)
        self.from_account = data.get("from", None)
        self.to_account = data.get("to", None)

