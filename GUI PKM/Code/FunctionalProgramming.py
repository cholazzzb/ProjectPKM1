a = 3
def some_func():
    global a
    a = 5

some_func()
print(a)
