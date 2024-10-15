
def introspection_info(obj):
    information = {'type': type(obj), 'attributes': dir(obj),
                   'method': [method for method in dir(obj) if callable(getattr(obj, method))],
                   'module': obj.__class__.__module__, 'doc': obj.__doc__}
    return information

r = introspection_info(45)
print(r)

class MyClass:

    def mymethod(self):
        pass

obj = MyClass
information = introspection_info(obj)

for key, value in information.items():
    print(f'{key}: {value}')