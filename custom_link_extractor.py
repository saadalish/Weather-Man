from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.lxmlhtml import Link, operator, partial


class CustomLinkExtractor(LinkExtractor):

    def __init__(
        self, tag="a", attr="href", process=None, unique=False, strip=True
    ):
        self.scan_tag = tag if callable(tag) else partial(operator.eq, tag)
        self.scan_attr = attr if callable(attr) else partial(operator.eq, attr)
        self.process_attr = process
        self.unique = unique
        self.strip = strip
        self.link_key = operator.attrgetter("url")

    def _canonicalize_link_url(self):
        return self

    def extract_links(self, response):

        next_page_url = None
        try:
            next_page_url = response.css('link[rel="next"]::attr(href)').extract()
            next_page_url = f"https://lemkus.com/{next_page_url[0]}"
            next_page_url = [Link(next_page_url)]
        except IndexError:
            pass
        finally:
            return next_page_url

    def _link_allowed(self, link):
        return True
