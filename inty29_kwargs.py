'''*args, **kwargs'''

def m1(*args,**kwargs):
    print('The type of args is ',type(args))
    print('The type of kwargs is ',type(kwargs))

m1()

dict = {'Name':'Bob','Age':'33','Sex':'Male'}

def someone(**kwargs):
    for key,value in kwargs.items():
        print(key,':\t',value)

someone(name='Rick',classroom='106')

# def someone(dic_someone):
#     for key,value in dic_someone.items():
#         print(key,':\t',value)
#
# someone(dict)