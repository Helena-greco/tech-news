from tech_news.database import find_news


# Ref: https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
# Ref: https://www.programiz.com/python-programming/methods/built-in/sorted
# Requisito 10
def top_5_news():
    all_news = find_news()
    ordered_by_comments = sorted(
        all_news, key=lambda comments: comments["comments_count"], reverse=True
    )
    news_list = []

    for news in ordered_by_comments[:5]:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
