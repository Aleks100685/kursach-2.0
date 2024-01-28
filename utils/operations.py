from datetime import datetime
import json



with open("transactions.json", "r", encoding="utf-8") as file:
    transactions_data = json.load(file)

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

# Загрузка данных из файла (предполагается, что у вас есть файл transactions.json)



# Преобразование данных в объекты Transaction
transactions = [Transaction(data) for data in transactions_data]

def display_last_transactions(transactions, n=5):
    # Сортируем транзакции по дате в обратном порядке
    sorted_transactions = sorted(
        [transaction for transaction in transactions if transaction.date],
        key=lambda x: datetime.strptime(x.date, "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=True
    )

    # Выводим последние n транзакций
    for transaction in sorted_transactions[:n]:
        print(f"{transaction.date.split('T')[0]} {transaction.description}")
        if transaction.from_account:
            print(f"{transaction.from_account} -> {transaction.to_account}")
        else:
            print(f"To: {transaction.to_account}")
        print(f"{transaction.amount} {transaction.currency}\n")

# Вывести последние 5 транзакций
display_last_transactions(transactions, n=5)