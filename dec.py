from functools import wraps

def prohibit_divide_by_zero(func):
   # @wraps(func)
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            raise ValueError('Cannot divide by zero')
        return func(*args, **kwargs)
    return wrapper

@prohibit_divide_by_zero
def divide(a, b):
    return a / b

print(divide(3,0))