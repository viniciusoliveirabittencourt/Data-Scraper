from xml.etree.ElementTree import Element, tostring
from report_interface import report_interface


class xml_report(report_interface):
    def create_report(dict):
        print("Generating xml file...")

        with open("xml_report.xml", "wb") as file:
            xml_node = Element("books")
            for book_name, book_price in dict.items():
                sup_node = Element("book")
                book_name_node = Element("book_name")
                book_name_node.text = book_name
                sup_node.append(book_name_node)
                book_price_node = Element("book_price")
                book_price_node.text = book_price
                sup_node.append(book_price_node)
                xml_node.append(sup_node)

            file.write(tostring(xml_node))

            print("Xml report done successfully.")
