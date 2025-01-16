import argparse
import os

from parsers.polish_python_parser import parse_polish_python

if __name__ == "__main__":
    command_parser = argparse.ArgumentParser(
        description="PolishPython Compiler and Executor. This tool compiles PolishPython scripts and optionally executes them."
    )

    command_parser.add_argument(
        "--file",
        required=True,
        help="Path to the input PolishPython script (required)."
    )
    command_parser.add_argument(
        "--output",
        default="./output",
        help="Path to the output file for the compiled script (optional). Defaults to './output'."
    )
    command_parser.add_argument(
        "--run",
        action="store_true",
        help="Flag to execute the compiled program after compilation."
    )

    args = command_parser.parse_args()

    code = parse_polish_python(args.file)

    if os.path.isdir(args.output) or not args.output.endswith(".py"):
        file_name = os.path.basename(args.file).replace(".ppy", ".py")
        output_file = os.path.join(args.output, file_name)  # noqa
    else:
        output_file = args.output

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(code)

    if args.run:
        exec(code)
