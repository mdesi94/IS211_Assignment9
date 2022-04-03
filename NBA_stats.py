import requests
from bs4 import BeautifulSoup as bs


def scraper(URL):
    # get/parse data from url
    r = requests.get(URL)
    soup = bs(r.text, features='lxml')

    # remove top header since it's unnecessary
    soup.find('tr', class_="over_header").decompose()

    # select only the table from webpage
    mvp_table = soup.find(id='mvp')

    # split/space out headers
    headers = mvp_table.find_all('th')
    print(
        f"{headers[1].text.strip():<19} {headers[2].text.strip():<10} "
        f"{headers[3].text.strip():<7} {headers[4].text.strip():<10}"
        f"{headers[5].text.strip():<10} {headers[6].text.strip():<10}"
        f"{headers[7].text.strip():<10} {headers[8].text.strip():<10} "
        f"{headers[9].text.strip():<7} {headers[10].text.strip():<10}"
        f"{headers[11].text.strip():<10} {headers[12].text.strip():<10}"
        f"{headers[13].text.strip():<10} {headers[14].text.strip():<10} "
        f"{headers[15].text.strip():<7} {headers[16].text.strip():<10}"
    )

    # split/space out each row
    rows = mvp_table.find_all('tr')
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<20}{cells[1].text.strip():<10}"
            f"{cells[2].text.strip():<10}{cells[3].text.strip():<10}"
            f"{cells[4].text.strip():<10}{cells[5].text.strip():<10}"
            f"{cells[6].text.strip():<10}{cells[7].text.strip():<10}"
            f"{cells[8].text.strip():<10}{cells[9].text.strip():<10}"
            f"{cells[10].text.strip():<10}{cells[11].text.strip():<10}"
            f"{cells[12].text.strip():<10}{cells[13].text.strip():<10}"
            f"{cells[14].text.strip():<10}{cells[15].text.strip():<10}"
        )


if __name__ == "__main__":
    URL = 'https://www.basketball-reference.com/awards/awards_2021.html'
    scraper(URL)