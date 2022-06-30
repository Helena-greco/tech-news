from tech_news.database import search_news


# Ref: https://www.mongodb.com/docs/manual/reference/operator/query/regex/
# Requisito 6
def search_by_title(title):
    titles = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    news_list = list()
    for news in titles:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    tags = search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    )
    news_list = list()
    for news in tags:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
