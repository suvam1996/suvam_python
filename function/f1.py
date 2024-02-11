# def printer():
#     print('hello world')
# def add(a,b):
#     return a+b
#
# printer()
# s=add(10,20)
# print(s)
#
# def variable_length_keywordarg(**kwargs):
#     for k in kwargs.items():
#         print(k,type(k))
#
#         # print(f'{k},{v}',type(k),type(v))
#
# variable_length_keywordarg(name='suvam',city='Bhadrak',pin=756100)

# from functools import reduce
# l=[10000,15000,12000,20000]
# var= reduce(lambda a,b:a+b,l)
# print(var)
def outer():
    print('outer')
    inner_function()

def inner_function():
    print('inner')


outer()