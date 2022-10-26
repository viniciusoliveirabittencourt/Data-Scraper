import json
from report_interface import report_interface


class json_report(report_interface):
    def create_report(dict):
        print("Generating json file...")

        with open("json_report.json", "w") as file:
            json.dump({"books": dict}, file)

            print("Json report done successfully.")
