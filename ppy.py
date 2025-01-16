import argparse
import os

from parsers.polish_python_parser import parse_polish_python

if __name__ == "__main__":
    command_parser = argparse.ArgumentParser(description="")

    command_parser.add_argument("--file", default="examples/example6.ppy", help="Path to the input file (required).")
    command_parser.add_argument("--output", default="./output", help="Path to the output file (optional).")
    command_parser.add_argument("--run", action="store_true", help="Flag to execute the program.")

    args = command_parser.parse_args()

    code = parse_polish_python(args.file)

    if os.path.isdir(args.output) or not args.output.endswith(".py"):
        file_name = os.path.basename(args.file).replace(".ppy", ".py")
        output_file = os.path.join(args.output, file_name) # noqa
    else:
        output_file = args.output

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(code)

    if args.run:
        exec(code)
