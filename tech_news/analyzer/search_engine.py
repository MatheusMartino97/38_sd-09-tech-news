from tech_news.database import db
import re


def format_return(news):
    return [(each_news["title"], each_news["url"]) for each_news in news]


def validate_date_regex(date):
    regex = re.search(r"(\d{4})-\d{2}-\d{2}", date)
    if regex is None or int(regex[1]) < 2000:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    news = db.news.find({"title": re.compile(title, re.IGNORECASE)})

    return format_return(news)


# Requisito 7
def search_by_date(date):
    validate_date_regex(date)

    news = db.news.find({"timestamp": {"$regex": date}})

    return format_return(news)


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
