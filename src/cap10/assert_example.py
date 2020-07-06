def sum(a, b):
    assert isinstance(a, int) and isinstance(b, int), f'a and b must be integer!\ntype a is {type(a)}\ntype b is {type(b)}'
    print(a + b)


sum(1, 2)
sum('12', 2)