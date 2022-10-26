import requests
from parsel import Selector
from json_report import json_report
from csv_report import csv_report
from xml_report import xml_report

link = "http://books.toscrape.com/catalogue/"
next_button = "page-1.html"
all_books = {}
number = 1

broke = False

while next_button:
    try:
        response = requests.get(link + next_button, timeout=3)
        selector = Selector(text=response.text)
        next_button = selector.css(".next a::attr(href)").get()
        books_cards = selector.css(
            ".product_pod .image_container a::attr(href)"
        ).getall()
        print(f"Getting books info, from page {number}...")
        for books in books_cards:
            new_response = requests.get(link + books, timeout=3)
            new_selector = Selector(text=new_response.text)
            book_name = new_selector.css(".product_main h1::text").get()
            book_price = new_selector.css(
                ".product_main .price_color::text"
            ).get()

            if book_name not in all_books:
                all_books[book_name] = book_price

        number += 1
    except requests.ConnectionError:
        print("We can't connet with website.")
        broke = True
        break

    except requests.ReadTimeout:
        print("We can't connet with website.")
        broke = True
        break

if broke:
    if len(all_books) == 0:
        print("Sorry, I couldn't get any books!")
    else:
        print("Here what I Got: \n", all_books)
else:
    print("Here are all_books that I find: ", all_books)

json_report.create_report(all_books)
csv_report.create_report(all_books)
xml_report.create_report(all_books)
