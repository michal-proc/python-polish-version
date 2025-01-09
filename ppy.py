from parsers.polish_python_parser import parse_polish_python

# TODO: arguments

if __name__ == "__main__":
    code = parse_polish_python("examples/example.ppy")
    print(code)
