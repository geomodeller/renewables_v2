import csv


def convert_to_csv(input_file, output_file):
    with open(input_file, "r") as txt_file, open(
        output_file, "w", newline=""
    ) as csv_file:
        reader = csv.reader(txt_file, delimiter="\t")
        writer = csv.writer(csv_file)

        for i, row in enumerate(reader):
            # Skip lines starting with '#'
            if not row or row[0].startswith("#") or row[0].startswith("5s"):
                continue
            # Skip second row (column width info)
            writer.writerow(row)
