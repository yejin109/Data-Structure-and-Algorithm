import time
import env


def partition(func):
    def wrap(*args, **kwargs):
        print('='*50)
        print('Function Name : ', func.__name__)
        print("Result are -->")
        res = func(*args, **kwargs)
        print('='*50)
        return res
    new_func = wrap
    new_func.__name__ = func.__name__
    return new_func


@partition
def print_attrs(obj, level='UserDefined'):
    for k, v in vars(obj).items():
        if level == 'All':
            print(k, v)
        elif level == 'UserDefined':
            if not k.startswith('__'):
                print(k, v)


@partition
def print_methods(obj, level='UserDefined'):
    for method in dir(obj):
        if callable(getattr(obj, method)):
            if level == 'All':
                print(method)
            elif level == 'UserDefined':
                if not method.startswith('__'):
                    print(method)


def check_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Runtime : {time.time()-start: .9f}s")
        return res
    new_func = wrap
    new_func.__name__ = func.__name__
    return new_func


@partition
@check_time
def test_func(func, *args, **kwargs, ):
    print('Target Function : ', func.__name__)
    print(f"Inputs : \n Argument : {args} \n Keyword Argument : {kwargs}")
    for i in range(env.TEST_ITERATION):
        res = func(*args, **kwargs)
        # if i == 0:
    print(f"Outputs : \n {res}, Iteration : {env.TEST_ITERATION}")
