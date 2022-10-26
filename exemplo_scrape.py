import requests
from parsel import Selector

link = "http://books.toscrape.com/catalogue/"
next_button = "page-1.html"
all_books = {}
number = 1

while next_button:
  response = requests.get(link + next_button)
  selector = Selector(text=response.text)
  next_button = selector.css(".next a::attr(href)").get()
  books_cards = selector.css(".product_pod .image_container a::attr(href)").getall()
  print(f"Obtendo as informações da página {number}...")
  for books in books_cards:
      new_response = requests.get(link + books)
      new_selector = Selector(text=new_response.text)
      book_name = new_selector.css(".product_main h1::text").get()
      book_price = new_selector.css(".product_main .price_color::text").get()

      if book_name not in all_books:
          all_books[book_name] = book_price

  number += 1

print("Aqui estão as informações pedidas: \n", all_books)
