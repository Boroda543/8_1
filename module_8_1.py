def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if isinstance(a, (int, float )) and isinstance(b, str):
            return str(a) + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + str(b)
        else:
            raise TypeError("Аргументы должны быть одног типа (число или строка)")

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456,7))