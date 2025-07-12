import scrapy
from scrapy_playwright.page import PageCoroutine

class AgodaSpider(scrapy.Spider):
    name = "agoda"
    custom_settings = {
        "PLAYWRIGHT_ENABLED": True,
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }

    def __init__(self, city='', **kwargs):
        super().__init__(**kwargs)
        self.city = city

    def start_requests(self):
        url = f"https://www.agoda.com/search?city={self.city}"
        yield scrapy.Request(
            url,
            meta={"playwright": True, "playwright_page_coroutines": [PageCoroutine("wait_for_selector", ".PropertyCard")],
            },
            callback=self.parse
        )

    def parse(self, response):
        for hotel in response.css(".PropertyCard"):
            yield {
                "name": hotel.css(".PropertyCard__HotelName::text").get(),
                "image": hotel.css("img::attr(src)").get(),
                "rating": hotel.css(".Review-score::text").get(),
                "price": hotel.css(".Price__Value::text").get(),
                "source": "Agoda.com",
                "url": response.url,
            }
