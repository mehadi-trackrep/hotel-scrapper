import scrapy
from scrapy_playwright.page import PageCoroutine

class BookingSpider(scrapy.Spider):
    name = "booking"
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
        url = f"https://www.booking.com/searchresults.html?ss={self.city}"
        yield scrapy.Request(
            url,
            meta={"playwright": True, "playwright_page_coroutines": [PageCoroutine("wait_for_selector", "div[data-testid='property-card']")]},
            callback=self.parse
        )

    def parse(self, response):
        for hotel in response.css("div[data-testid='property-card']"):
            yield {
                "name": hotel.css("div[data-testid='title']::text").get(),
                "image": hotel.css("img::attr(src)").get(),
                "rating": hotel.css("div.b5cd09854e.d10a6220b4::text").get(),
                "price": hotel.css("span.fcab3ed991.bd73d13072::text").get(),
                "source": "Booking.com",
                "url": response.url,
            }
