from tech_news.database import db
import re


def get_formated_news(query):
    news = db.news.find(query)
    return [(each_news["title"], each_news["url"]) for each_news in news]


def validate_date_regex(date):
    regex = re.search(r"(\d{4})-\d{2}-\d{2}", date)
    if regex is None or int(regex[1]) < 2000:
        raise ValueError("Data inválida")


# Requisito 6
def search_by_title(title):
    return get_formated_news({"title": re.compile(title, re.IGNORECASE)})


# Requisito 7
def search_by_date(date):
    validate_date_regex(date)

    return get_formated_news({"timestamp": {"$regex": date}})


# Requisito 8
def search_by_source(source):
    return get_formated_news({"sources": re.compile(source, re.IGNORECASE)})


# Requisito 9
def search_by_category(category):
    query = {"categories": re.compile(category, re.IGNORECASE)}
    return get_formated_news(query)
