import json
from func.utils import *  # импортируем функции из файла
from func import *


info_file = load_file('operations.json')
sorted_data = executed_sorted_file(info_file)
cardoperations = Cardoperations(sorted_data)
cardoperations.operation_count()
cardoperations.date_format()
cardoperations.card_format()
cardoperations.count_format()


def print_transaction(transactions):
    for transaction in transactions:
        date = transaction.get('date')
        operation = transaction.get('description')
        card_number = transaction.get('from')
        count = transaction.get('to')
        amount = transaction.get('operationAmount').get('amount')
        currency = transaction.get('operationAmount').get('currency').get('name')
        if operation == 'Открытие вклада':
            print(f'{date} {operation}')
            print(f'{count}')
            print(f'{amount}{currency}')
            print()
        else:
            print(f'{date} {operation}')
            print(f'{card_number}->{count}')
            print(f'{amount}{currency}')
            print()


print_transaction(cardoperations.operation)
