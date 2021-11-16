from tech_news.database import find_news
import operator
from collections import Counter


# Requisito 10
def top_5_news():
    news = find_news()

    if (news):
        for item in news:
            item["score"] = item["shares_count"] + item["comments_count"]

        sorted_list = (
            sorted(news, key=operator.itemgetter("score"), reverse=True)
        )

        top_5_news = sorted_list[:5]

        return [(item["title"], item["url"]) for item in top_5_news]

    return []


# Requisito 11
def top_5_categories():
    news = find_news()
    if (news):
        categories = []

        for item in news:
            categories.extend(item["categories"])

        categories_count = list(Counter(categories).keys())
        categories_count.sort()

        return categories_count[:5]
    return []
