import requests
from bs4 import BeautifulSoup as bs


def scrape_page(URL):
    # get/parse data from url
    r = requests.get(URL)
    soup = bs(r.text, features='lxml')

    # extract table from webpage
    result_table = soup.find_all("table", class_="wikitable sortable")

    # get rows
    rows = result_table[0].find_all('tr')

    # get and format headers
    headers = rows[0].find_all('th')
    print(
        f"{headers[0].text.strip():<15} {headers[1].text.strip():<40} "
        f"{headers[2].text.strip():<35} {headers[3].text.strip():<15}"
        f"{headers[4].text.strip():<15}"
    )

    # Get all the data and format
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} {cells[1].text.strip():<40} "
            f"{cells[2].text.strip():<35} {cells[3].text.strip():<15}"
            f"{cells[4].text.strip():<15}"
        )


if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions'
    scrape_page(URL)