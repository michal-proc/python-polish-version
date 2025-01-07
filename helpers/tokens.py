import token
import keyword

tokens = {name: value for name, value in vars(token).items() if not name.startswith("_") and isinstance(value, int)}

for keyword in keyword.kwlist:
    print(keyword.upper() + ": '';")
