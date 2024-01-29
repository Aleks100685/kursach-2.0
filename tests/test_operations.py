import unittest
from unittest.mock import patch
from main import Transaction, display_last_transactions


class TestTransactions(unittest.TestCase):

    def test_transaction_creation(self):
        data = {
            "id": 123,
            "state": "EXECUTED",
            "date": "2022-01-19T12:34:56.789",
            "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}},
            "description": "Test Transaction",
            "from": "Account123",
            "to": "Account456"
        }
        transaction = Transaction(data)

        self.assertEqual(transaction.id, 123)
        self.assertEqual(transaction.state, "EXECUTED")
        self.assertEqual(transaction.date, "2022-01-19T12:34:56.789")
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.currency, "USD")
        self.assertEqual(transaction.description, "Test Transaction")
        self.assertEqual(transaction.from_account, "Account123")
        self.assertEqual(transaction.to_account, "Account456")

    def test_display_last_transactions(self):
        # Создаем тестовые данные
        transactions_data = [
            {"id": 1, "state": "EXECUTED", "date": "2022-01-19T12:00:00.000", "operationAmount": {"amount": "50.0", "currency": {"name": "USD", "code": "USD"}}, "description": "Transaction 1", "from": "AccountA", "to": "AccountB"},
            {"id": 2, "state": "EXECUTED", "date": "2022-01-19T13:00:00.000", "operationAmount": {"amount": "75.0", "currency": {"name": "USD", "code": "USD"}}, "description": "Transaction 2", "from": "AccountB", "to": "AccountC"},
            {"id": 3, "state": "EXECUTED", "date": "2022-01-19T14:00:00.000", "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}}, "description": "Transaction 3", "from": "AccountC", "to": "AccountD"}
        ]

        # Преобразуем данные в объекты Transaction
        transactions = [Transaction(data) for data in transactions_data]

        # Создаем тестовый вывод
        expected_output = [
            "2022-01-19 Transaction 3",
            "AccountC -> AccountD",
            "100.0 USD\n",
            "2022-01-19 Transaction 2",
            "AccountB -> AccountC",
            "75.0 USD\n",
            "2022-01-19 Transaction 1",
            "AccountA -> AccountB",
            "50.0 USD\n"
        ]

        # Перехватываем вывод
        with patch('builtins.print') as mock_print:
            # Вызываем функцию
            display_last_transactions(transactions, n=3)

            # Проверяем, что вывод соответствует ожидаемому
            self.assertEqual(mock_print.call_count, len(expected_output))
            for call_args, expected_output_line in zip(mock_print.call_args_list, expected_output):
                self.assertEqual(call_args[0][0], expected_output_line)

if __name__ == '__main__':
    unittest.main()