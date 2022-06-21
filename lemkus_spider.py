import json
import re

from scrapy.spiders import CrawlSpider, Rule
import scrapy

from custom_link_extractor import CustomLinkExtractor


class LemkusSpider(CrawlSpider):
    name = "lemkus-spider"
    product_collection_id = re.compile('var page_id = (.*?);')
    start_urls = [
        'https://lemkus.com/collections/sneakers',
        'https://lemkus.com/collections/apparel',
        'https://lemkus.com/collections/kids'
    ]

    rules = [Rule(CustomLinkExtractor(), callback='parse', follow=True)]

    def parse(self, response):
        current_page_no = self.get_current_page_no_to_scrape(response)
        product_collection_id = self.get_product_collection_id(response)
        request_url_to_get_product_details = (
            f'https://filter-v5.globosoftware.net/filter?callback=jQuery3600522409738760953_1655462185424&'
            f'filter_id=26694&shop=lemkus-staging.myshopify.com&collection={product_collection_id}&'
            f'sort_by=manual&page={current_page_no}&event=all&_=1655462185425'
        )
        yield scrapy.Request(request_url_to_get_product_details, callback=self.parse_product)

    @staticmethod
    def parse_product(response):
        products = json.loads(response.css('p').re_first('{.+}'))
        for product in products["products"]:
            yield {
                "title": product.get("title"),
                "category": product.get("product_type"),
                "vendor": product.get("vendor"),
                "src": f"https://lemkus.com/collections/{product.get('product_type')}/products/{product.get('handle')}",
                "details": product.get("body_html"),
                "available-sizes": product.get("variants"),
                "images": product.get("images")
            }

    @staticmethod
    def get_current_page_no_to_scrape(response):
        page_no = None
        try:
            current_page_url = response.css('link[rel="canonical"]::attr(href)').extract()[0].split('?')
            url, page_no = current_page_url.split("?")
            page_no = int(current_page_url[-1].split("=")[-1])
        except IndexError:
            pass
        except ValueError:
            page_no = 1  # first page
        finally:
            return page_no

    def get_product_collection_id(self, response):
        return response.css('script::text').re_first(self.product_collection_id)
