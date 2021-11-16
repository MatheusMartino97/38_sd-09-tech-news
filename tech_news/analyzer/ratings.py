from tech_news.database import find_news
import operator


# Requisito 10
def top_5_news():
    news = find_news()
    news_with_score = []

    if (news):
        for each_news in news:
            each_news["score"] = news["shares_count"] + news["comments_count"]
            news_with_score.append(each_news)

    sorted_list = (
        sorted(news_with_score, key=operator.itemgetter("score"), reverse=True)
    )

    return sorted_list[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
