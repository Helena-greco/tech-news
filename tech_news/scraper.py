import time
import requests
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text

        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    response = selector.css(".cs-overlay-link::attr(href)").getall()
    return response


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    response = selector.css(".next.page-numbers::attr(href)").get()
    return response


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    news = dict()

    news["url"] = selector.css("[rel='canonical']::attr(href)").get()
    news["title"] = selector.css("h1.entry-title::text").get()
    news["timestamp"] = selector.css("li.meta-date::text").get()
    news["writer"] = selector.css("a.url.fn.n::text").get()
    news["comments_count"] = 0
    # sel.xpath("string(//a[1])").getall() # convert it to string
    # Ref: https://docs.scrapy.org/en/latest/topics/selectors.html
    news["summary"] = selector.xpath("string(//div[@class='entry-content']/p)").get()
    news["tags"] = selector.css("[rel='tag']::text").getall()
    news["category"] = selector.css(".category-style .label::text").get()

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
