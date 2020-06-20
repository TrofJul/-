# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
    # Нужно реализовать конструктор
    # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
    # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
    # Например: ignore_case = True, Aбв и АБВ разные строки
    # ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
    # По-умолчанию ignore_case = False
        self.unique = []
        if 'ignore_case' not in kwargs.keys():
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']
        self.items = iter(items)

    def __next__(self):
        while True:
            item = self.items.__next__()
            compare_item = None

            if self.ignore_case and type(item) is str:
                compare_item = item.lower()
            else:
                compare_item = item

            if compare_item not in self.unique:
                self.unique.append(compare_item)
                return item

    def __iter__(self):
        return self


