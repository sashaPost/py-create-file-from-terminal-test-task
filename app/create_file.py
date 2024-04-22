import sys
import os
import datetime


def create_file(directory_path, file_name):
    """Creates a file with content in specified directory."""
    os.makedirs(directory_path, exist_ok=True)

    full_path = os.path.join(directory_path, file_name)

    with open(full_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    directory_path = "."
    file_name = None

    for i, arg in enumerate(sys.argv[1:]):
        if arg == "-d":
            directory_path = os.path.join(*sys.argv[i + 2:])
        elif arg == "-f":
            if file_name is not None:
                print("Error: Multiple file names specified.")
                sys.exit(1)
            file_name = sys.argv[i + 2]

    if file_name is None:
        print("Error: File name is required.")
        sys.exit(1)

    create_file(directory_path, file_name)
