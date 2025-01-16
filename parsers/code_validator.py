import json
import os
import subprocess

TEMP_FILE_PATH = "temp_code.py"


def validate_code(code):
    try:
        with open(TEMP_FILE_PATH, "w") as temp_file:
            temp_file.write(code)

        result = subprocess.run(["flake8", "--format=json", TEMP_FILE_PATH], capture_output=True, text=True)
        errors = json.loads(result.stdout)
    finally:
        if os.path.exists(TEMP_FILE_PATH):
            os.remove(TEMP_FILE_PATH)

    return errors
