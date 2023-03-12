from datetime import datetime


def print_even_values(collection: list):
    if len(collection) == 0:
        return

    if len(collection) == 1:
        if collection[0] % 2 == 0:
            pass#print(collection[0])
        return

    if collection[0] % 2 == 0:
        pass#print(collection[0])
    print_even_values(collection[1:])


def print_even_values_2(collection: list):
    if len(collection) == 0:
        return

    if collection[0] % 2 == 0:
        pass#print(collection[0])
    print_even_values(collection[1:])

start = datetime.now()

for _ in range(10000):
    print_even_values_2([i for i in range (900)])

end = datetime.now()

print('Без дополнительной проверки: ', (end - start) / 10000)

start = datetime.now()

for _ in range(10000):
    print_even_values([i for i in range (900)])

end = datetime.now()

print('C дополнительной проверкой: ', (end - start) / 10000)