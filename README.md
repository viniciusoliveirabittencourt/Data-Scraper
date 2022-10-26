# Data Scraper

A little project, just to train data scraper, using Python with libs Requests and Parsel.

> To this project, I'm using **Pyhton - 3.8.10**, **Requests - 2.28.1**, **Parsel - 1.16.0**

# Run in your machine

To run it, first you will need clone this repo, after this you will enter the dir create by git clone and run the follow command to start a virtual environment:

- `python3 -m venv .venv && source .venv/bin/activate`

after this, you need to run the follow command to install the dependencies:

- `python3 -m pip install -r dev-requirements.txt`

and you can run this command to run the application:

- `python3 -m exemplo_scrape.py`

---

# Application

The application make a data scraper on site http://books.toscrape.com/, where the goal are get the names and correlate with prices and gave reports in csv, xml and json.

## CSV Report

The csv report will create a csv file called `csv_report.csv`, where the response will be like this:

```csv
book_name, book_price
A Light in the Attic,£51.77
...
```

## JSON Report

The json report will create a json file called `json_report.json`, where the response will be like this:

```json
  {
    books: {
      "A Light in the Attic": "£51.77",
      ...
    }
  }
```

## XML Report

The json report will create a xml file called `xml_report.xml`, where the response will be like this:

```xml
  <books>
    <book>
      <book_name>A Light in the Attic</book_name>
      <book_price>£51.77</book_price>
    </book>
    ...
  </books>
```