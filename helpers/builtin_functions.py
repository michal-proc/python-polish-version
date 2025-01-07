import builtins

# At the moment, project supports only built-in functions
for name in dir(builtins):
    obj = getattr(builtins, name)
    if callable(obj) and not name.startswith('__') and not name.endswith('Error') and not name.endswith('Warning'):
        print(name.upper())
