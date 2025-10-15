# main.py
import sys
from parse_temps import parse_raw_temps
from piecewise import write_interpolation_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the temperature data
    times = []
    core_data = [[] for _ in range(4)]  # 4 cores

    with open(input_file, "r") as infile:
        for time, readings in parse_raw_temps(infile):
            times.append(time)
            for i, temp in enumerate(readings):
                core_data[i].append(temp)

    # Generate one output file per core
    for i, y_values in enumerate(core_data):
        output_filename = f"{input_file[:-4]}-core-{i:02}.txt"
        write_interpolation_file(output_filename, times, y_values)
        print(f"Created {output_filename}")


if __name__ == "__main__":
    main()
