chars = ['A', 'B', 'C'] # Список
fruit = ('Apple', 'Banana', 'Cherry')   # Кортеж
dict = {'name': 'Mike', 'ref': 'Python', 'sys': 'Win'}  # Словарь

print('\nElements:\t', end=' ')
for item in chars:
    print(item, end=' ')

print('\nEnumerated:\t', end=' ')
for item in enumerate(chars):
    print(item, end=' ')

print('\nZipped:\t', end=' ')
for item in zip(chars, fruit):
    print(item, end=' ')

print( '\nPaired:' )
for key, value in dict.items() :
    print( key , '=' , value )

