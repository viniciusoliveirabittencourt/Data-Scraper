import csv
from report_interface import report_interface


class csv_report(report_interface):
    def create_report(dict):
        print("Generating csv file...")

        with open("csv_report.csv", "w") as file:

            headers = ["book_name", "book_price"]

            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for book_name, book_price in dict.items():
                row = {"book_name": book_name, "book_price": book_price}
                writer.writerow(row)

            print("Csv report done successfully.")
