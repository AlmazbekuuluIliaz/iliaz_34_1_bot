from parsel import Selector
import requests


class ExchangeRateScraper:
    URL = 'https://kurs.kg/dollar/'
    KICB_TITLE_XPATH = '//tr[@class="ninja_table_row_13 nt_row_id_13"]/td/a/text()'
    KICB_DOLLAR_RATES_XPATH = '//tr[@class="ninja_table_row_13 nt_row_id_13"]/td[2]/text()'
    UNIVERSAL_DOLLAR_BUY_RATE_XPATH = '//tr[@class="ninja_table_row_{row} nt_row_id_{row}"]/td[2]/text()'
    UNIVERSAL_DOLLAR_SELL_RATE_XPATH = '//tr[@class="ninja_table_row_{row} nt_row_id_{row}"]/td[3]/text()'

    def parse_rate(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        for row in range(22):
            buy_rate = tree.xpath(self.UNIVERSAL_DOLLAR_BUY_RATE_XPATH.format(row=row)).extract_first()
            sell_rate = tree.xpath(self.UNIVERSAL_DOLLAR_SELL_RATE_XPATH.format(row=row)).extract_first()
            print(buy_rate)
            print(sell_rate)


if __name__ == "__main__":
    scraper = ExchangeRateScraper()
    scraper.parse_rate()