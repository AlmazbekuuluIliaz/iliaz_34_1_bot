"https://rezka.ag/cartoons/fantasy/"
from parsel import Selector
import requests


class CartoonScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    URL = "https://rezka.ag/cartoons/page/{page}/"
    CARTOON_LINK_XPATH = '//div[@class="b-content__inline_item"]/@data-url'

    def parse_page(self):
        for page in range(1, 10):
            html = requests.get(url=self.URL.format(page=page), headers=self.headers).text
            print(f'***PAGE: {self.URL.format(page=page)}')
            self.parse_data(html=html)

    def parse_data(self, html):
        tree = Selector(text=html)
        links = tree.xpath(self.CARTOON_LINK_XPATH).extract()
        for link in links:
            print(link)


if __name__ == "__main__":
    scraper = CartoonScraper()
    scraper.parse_page()