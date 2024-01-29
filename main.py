import json
from utils.operations import Transaction
from datetime import datetime

with open("C:\\Users\\Sasha\\pythonProject2\\utils\\transactions.json", "r", encoding="utf-8") as file:
    transactions_data = json.load(file)

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

