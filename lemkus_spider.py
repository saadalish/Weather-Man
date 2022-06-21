import json
import re
import scrapy


class LemkusSpider(scrapy.Spider):
    name = "lemkus-spider"
    start_urls = [
        'https://lemkus.com/collections/sneakers',
        'https://lemkus.com/collections/apparel',
        'https://lemkus.com/collections/kids'
    ]

    @staticmethod
    def get_current_page_no_to_scrap(response):
        current_page_url = response.css('link[rel="canonical"]::attr(href)').extract()[0].split('?')
        if len(current_page_url) < 2:
            return 1
        return int(current_page_url[-1].split("=")[-1])

    @staticmethod
    def get_next_page_no_to_scrap(response):
        next_page_url = response.css('link[rel="next"]::attr(href)').extract()
        if len(next_page_url) > 0:
            return int(next_page_url[0].split('?')[-1].split("=")[-1])
        return None

    @staticmethod
    def get_product_collection_id(response):
        collection_id_pattern_in_response = re.compile('var page_id = (.*?);')
        return response.css('script::text').re_first(collection_id_pattern_in_response)

    def parse(self, response):
        current_page_no = self.get_current_page_no_to_scrap(response)
        product_collection_id = self.get_product_collection_id(response)
        request_url_to_extract_specific_product_details = (
            f'https://filter-v5.globosoftware.net/filter?callback=jQuery3600522409738760953_1655462185424&'
            f'filter_id=26694&shop=lemkus-staging.myshopify.com&collection={product_collection_id}&'
            f'sort_by=manual&page={current_page_no}&event=all&_=1655462185425'
        )
        yield scrapy.Request(request_url_to_extract_specific_product_details, callback=self.parse_product)

        next_page = self.get_next_page_no_to_scrap(response)
        if next_page:
            next_page_url = f'{response.url.split("?")[0]}?page={next_page}'
            yield scrapy.Request(next_page_url, callback=self.parse)

    @staticmethod
    def parse_product(response):
        products_dict = json.loads(response.css('p').re_first('{.+}'))
        for product in products_dict["products"]:
            yield {
                "title": product.get("title"),
                "category": product.get("product_type"),
                "vendor": product.get("vendor"),
                "details": product.get("body_html"),
                "available-sizes": product.get("variants"),
                "images": product.get("images")
            }
