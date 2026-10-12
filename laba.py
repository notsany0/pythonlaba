def simple_decore(fn):
    def wrapper(*args, **kwargs):
        print('Before')
        val=fn(*args, **kwargs)
        print('After')
        return val
    return wrapper

@simple_decore
def first(a):
    print('Test 1', a)
@simple_decore
def second(a):
    print('Test 2', a)


print(second(1))

