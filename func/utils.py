import json
from datetime import datetime


def load_file(filename):
    """
    Загружает инфу из файла json
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def executed_sorted_file(file):
    """
    Добавляет в список new_file только операции со статусом 'EXECUTED' и сортирует по убыванию даты
    """
    new_file = []
    for i in file:
        for k, v in i.items():
            if v == 'EXECUTED':
                new_file.append(i)
    sorted_data = sorted(new_file, key=lambda x: x['date'], reverse=True)  # сортировка списка по дате
    return sorted_data


class Cardoperations:

    def __init__(self, info_list):
        self.info_list = info_list
        self.operation = []

    def operation_count(self):
        """
        Первые 5 выполненных (EXECUTED) операций
        """
        self.operation.extend(self.info_list[0:5])

    def date_format(self):
        """
        Дата перевода представлена в формате ДД.ММ.ГГГГ
        """
        for i in range(len(self.operation)):
            if 'date' in self.operation[i]:
                datetime_obj = datetime.strptime(self.operation[i]['date'], '%Y-%m-%dT%H:%M:%S.%f')
                self.operation[i]['date'] = datetime_obj.strftime('%d.%m.%Y')
        return self.operation

    def card_format(self):
        for i in self.operation:
            for k, v in i.items():
                if k == 'from':
                    parts = v.split()
                    if parts[0] == 'Maestro':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + masked
                    if parts[0] == 'МИР':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + masked
                    if parts[0] == 'Visa':
                        masked = parts[2][:4] + ' ' + parts[2][4:6] + '** **** ' + parts[2][-4:]
                        i[k] = parts[0] + ' ' + parts[1] + ' ' + masked
                    if parts[0] == 'MasterCard':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + masked
                    if parts[0] == 'Счет':
                        masked = ' **' + parts[1][-4:]
                        i[k] = parts[0] + masked
                else:
                    None
        return self.operation

    def count_format(self):
        """
        Номер счета замаскирован и не отображается целиком в формате **XXXX
        """
        for i in self.operation:
            for k, v in i.items():
                if k == 'to':
                    parts = v.split(' ')
                    if parts[0] == 'Счет':
                        masked = ' **' + parts[1][-4:]
                        i[k] = parts[0] + masked
                    if parts[0] == 'Visa':
                        masked = parts[2][:4] + ' ' + parts[2][4:6] + '** **** ' + parts[2][-4:]
                        i[k] = parts[0] + ' ' + parts[1] + ' ' + masked
                    if parts[0] == 'МИР':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + masked
                    if parts[0] == 'Maestro':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + parts[1] + ' ' + masked
                    if parts[0] == 'MasterCard':
                        masked = parts[1][:4] + ' ' + parts[1][4:6] + '** **** ' + parts[1][-4:]
                        i[k] = parts[0] + ' ' + parts[1] + ' ' + masked
                else:
                    None
        return self.operation

