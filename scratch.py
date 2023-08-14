def my_decorator(func):
    def wrapper():
        print('This is happening before the function is called')
        func()
        print('This is happening after the function is called')
    return wrapper

@my_decorator
def say_hello():
    print('Hello how are you today?')

say_hello()

from app import format_name
print(format_name('jamie', 'marwell'))