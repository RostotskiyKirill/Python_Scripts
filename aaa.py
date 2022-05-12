def outer_func ():
    # Определение функции внутри другой
    # функции.
    def inner_func ():
        return 'some'

    return inner_func()


print(outer_func())  # some


def get_my_class ():
    # Определение класса внутри определения
    # функции.
    class MyClass:
        my_attr = 1

    return MyClass


my_class = get_my_class()
print(my_class.my_attr)  # 1))