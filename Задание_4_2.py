import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    input_file = open(INPUT_FILENAME, "r")
    output_file = open(OUTPUT_FILENAME, "w")
    reader = csv.DictReader(input_file)
    res = []
    for row in reader:
        res.append(row)
    json.dump(res, output_file, indent=4)
    input_file.close()
    output_file.close()
if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
