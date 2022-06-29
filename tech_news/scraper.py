import time
import requests
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
