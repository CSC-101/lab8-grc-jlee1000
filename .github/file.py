#task 2
import sys

def create_input_file():
    """Creates a sample input file named 'input.txt' for testing.
    """
    file_name = "input.txt"
    sample_data = """1.2 3.4
5.0 7.0
invalid 2.0
10.5 4.5
4.5"""
    with open(file_name, "w") as file:
        file.write(sample_data)
    print(f"Sample input file '{file_name}' created.")


def process_file(file_name):
    """Processes a file, computes sums for lines with two float values, and prints results or errors.

    input: (str) Name of the file to process.
    """
    try:
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    parts = line.split()
                    if len(parts) != 2:
                        raise ValueError("Line does not contain exactly two values.")

                    num1, num2 = map(float, parts)
                    print(f"Line {line_number}: {num1 + num2}")
                except ValueError as e:
                    print(f"Error on line {line_number}: {e}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' cannot be opened.")
        sys.exit(1)


def main():
    create_input_file()

    if len(sys.argv) != 2:
        print("Error: Please provide a file name as a command-line argument.")
        sys.exit(1)

    process_file(sys.argv[1])


if __name__ == "__main__":
    main()
